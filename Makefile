# This Makefile is only used by developers.
PYVER:=2.7
PYTHON:=python$(PYVER)
VERSION:=$(shell $(PYTHON) setup.py --version)
MAINTAINER:=$(shell $(PYTHON) setup.py --maintainer)
AUTHOR:=$(shell $(PYTHON) setup.py --author)
APPNAME:=$(shell $(PYTHON) setup.py --name)
LAPPNAME:=$(shell echo $(APPNAME)|tr "[A-Z]" "[a-z]")
ARCHIVE_SOURCE:=$(LAPPNAME)-$(VERSION).tar.gz
ARCHIVE_WIN32:=$(LAPPNAME)-$(VERSION).exe
GITUSER:=wummel
GITREPO:=$(LAPPNAME)
HOMEPAGE:=$(HOME)/public_html/$(LAPPNAME).git
DEBUILDDIR:=$(HOME)/projects/debian/official
DEBORIGFILE:=$(DEBUILDDIR)/$(LAPPNAME)_$(VERSION).orig.tar.gz
DEBPACKAGEDIR:=$(DEBUILDDIR)/$(LAPPNAME)-$(VERSION)
PY_FILES_DIRS := dosage dosagelib scripts tests
PY2APPOPTS ?=
# Default pytest options:
# Do not use parallel testing with -n: it makes some tests fail since
# some web servers have limits on the number of parallel connections.
# Also note that using -n silently swallows test creation exceptions like
# import errors.
PYTESTOPTS?=--resultlog=testresults.txt --tb=short --durations=0
CHMODMINUSMINUS:=--
# directory or file with tests to run
TESTS ?= tests
# set test options, eg. to "--verbose"
TESTOPTS=

all:

chmod:
	-chmod -R a+rX,u+w,go-w $(CHMODMINUSMINUS) *
	find . -type d -exec chmod 755 {} \;

dist:
	[ -d dist ] || mkdir dist
	git archive --format=tar --prefix=$(LAPPNAME)-$(VERSION)/ HEAD | gzip -9 > dist/$(ARCHIVE_SOURCE)
	[ ! -f ../$(ARCHIVE_WIN32) ] || cp ../$(ARCHIVE_WIN32) dist

sign:
	[ -f dist/$(ARCHIVE_SOURCE).asc ] || gpg --detach-sign --armor dist/$(ARCHIVE_SOURCE)
	[ -f dist/$(ARCHIVE_WIN32).asc ] || gpg --detach-sign --armor dist/$(ARCHIVE_WIN32)

upload:
	github-upload $(GITUSER) $(GITREPO) \
	  dist/$(ARCHIVE_SOURCE) dist/$(ARCHIVE_WIN32) \
	  dist/$(ARCHIVE_SOURCE).asc dist/$(ARCHIVE_WIN32).asc

testresults:
	scripts/mktestpage.py testresults.txt $(HOMEPAGE)/content

homepage:
# update metadata
	@echo "version: $(VERSION)" > $(HOMEPAGE)/info.yaml
	@echo "name: $(APPNAME)" >> $(HOMEPAGE)/info.yaml
	@echo "lname: $(LAPPNAME)" >> $(HOMEPAGE)/info.yaml
	@echo "maintainer: $(MAINTAINER)" >> $(HOMEPAGE)/info.yaml
	@echo "author: $(AUTHOR)" >> $(HOMEPAGE)/info.yaml
# generate static files
	$(MAKE) -C doc
	cp doc/$(LAPPNAME).1.html $(HOMEPAGE)/content
	make -C $(HOMEPAGE) gen

release: distclean releasecheck
	$(MAKE) dist sign upload homepage tag register deb

tag:
	git tag upstream/$(VERSION)
	git push --tags origin upstream/$(VERSION)

register:
	@echo "Register at Python Package Index..."
	$(PYTHON) setup.py register
	@echo "Submit to freecode..."
	freecode-submit < $(LAPPNAME).freecode

releasecheck: check
	@if egrep -i "xx\.|xxxx|\.xx" doc/changelog.txt > /dev/null; then \
	  echo "Could not release: edit doc/changelog.txt release date"; false; \
	fi
	@if [ ! -f ../$(ARCHIVE_WIN32) ]; then \
	  echo "Missing WIN32 distribution archive at ../$(ARCHIVE_WIN32)"; \
	  false; \
	fi
	@if ! grep "Version: $(VERSION)" $(LAPPNAME).freecode > /dev/null; then \
	  echo "Could not release: edit $(LAPPNAME).freecode version"; false; \
	fi
	$(PYTHON) setup.py check --restructuredtext

# The check programs used here are mostly local scripts on my private system.
# So for other developers there is no need to execute this target.
check:
	check-copyright
	check-pofiles -v
	py-tabdaddy
	py-unittest2-compat tests/
	$(MAKE) doccheck
	$(MAKE) pyflakes

doccheck:
	py-check-docstrings --force \
	  dosagelib/*.py \
	  dosage \
	  scripts \
	  *.py

pyflakes:
	pyflakes $(PY_FILES_DIRS)

count:
	@sloccount $(PY_FILES_DIRS)

clean:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete
	rm -rf build dist

distclean: clean
	rm -rf build dist $(APPNAME).egg-info $(LAPPNAME).prof test.sh
	rm -f _$(APPNAME)_configdata.py MANIFEST

localbuild:
	$(PYTHON) setup.py build

test:	localbuild
	env LANG=en_US.utf-8 http_proxy="" $(PYTHON) -m pytest $(PYTESTOPTS) $(TESTOPTS) $(TESTS)

deb:
# build a debian package
	[ -f $(DEBORIGFILE) ] || cp dist/$(ARCHIVE_SOURCE) $(DEBORIGFILE)
	sed -i -e 's/VERSION_$(LAPPNAME):=.*/VERSION_$(LAPPNAME):=$(VERSION)/' $(DEBUILDDIR)/$(LAPPNAME).mak
	[ -d $(DEBPACKAGEDIR) ] || (cd $(DEBUILDDIR); \
	  patool extract $(DEBORIGFILE); \
	  cd $(CURDIR); \
	  git checkout debian; \
	  cp -r debian $(DEBPACKAGEDIR); \
	  git checkout master)
	$(MAKE) -C $(DEBUILDDIR) $(LAPPNAME)_clean $(LAPPNAME)

update-copyright:
# update-copyright is a local tool which updates the copyright year for each
# modified file.
	update-copyright --holder="$(MAINTAINER)"

changelog:
# github-changelog is a local tool which parses the changelog and automatically
# closes issues mentioned in the changelog entries.
	github-changelog $(DRYRUN) $(GITUSER) $(GITREPO) doc/changelog.txt

.PHONY: update-copyright deb test clean distclean count pyflakes changelog
.PHONY: doccheck check releasecheck release dist chmod localbuild sign register tag
