# This Makefile is only used by developers.
# See doc/install.txt on how to install dosage
PYTHON:=python
VERSION:=$(shell $(PYTHON) setup.py --version)
MAINTAINER:=$(shell $(PYTHON) setup.py --maintainer)
AUTHOR:=$(shell $(PYTHON) setup.py --author)
APPNAME:=$(shell $(PYTHON) setup.py --name)
ARCHIVE_SOURCE:=$(APPNAME)-$(VERSION).tar.gz
ARCHIVE_WIN32:=$(APPNAME)-$(VERSION).exe
GITUSER:=wummel
GITREPO:=$(APPNAME)
HOMEPAGE:=$(HOME)/public_html/dosage-webpage.git
WEBMETA:=doc/web/app.yaml
DEBUILDDIR:=$(HOME)/projects/debian/official
DEBORIGFILE:=$(DEBUILDDIR)/$(APPNAME)_$(VERSION).orig.tar.gz
DEBPACKAGEDIR:=$(DEBUILDDIR)/$(APPNAME)-$(VERSION)
# Default pytest options
# Note that using -n silently swallows test creation exceptions like
# import errors.
PYTESTOPTS?=--resultlog=testresults.txt --tb=short -n10
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
	$(PYTHON) setup.py sdist --formats=tar
	gzip --best dist/$(APPNAME)-$(VERSION).tar
	[ ! -f ../$(ARCHIVE_WIN32) ] || cp ../$(ARCHIVE_WIN32) dist

sign:
	[ -f dist/$(ARCHIVE_SOURCE).asc ] || gpg --detach-sign --armor dist/$(ARCHIVE_SOURCE)
	[ -f dist/$(ARCHIVE_WIN32).asc ] || gpg --detach-sign --armor dist/$(ARCHIVE_WIN32)

upload:	upload_source upload_binary

upload_source:
	twine upload dist/$(ARCHIVE_SOURCE) dist/$(ARCHIVE_SOURCE).asc

upload_binary:
	cp dist/$(ARCHIVE_WIN32) dist/$(ARCHIVE_WIN32).asc \
	  $(HOMEPAGE)/dist

update_webmeta:
# update metadata
	@echo "version: \"$(VERSION)\"" > $(WEBMETA)
	@echo "name: \"$(APPNAME)\"" >> $(WEBMETA)
	@echo "maintainer: \"$(MAINTAINER)\"" >> $(WEBMETA)
	@echo "author: \"$(AUTHOR)\"" >> $(WEBMETA)
	git add $(WEBMETA)
	-git commit -m "Updated webpage meta info"

homepage: update_webmeta
# update documentation and release website
	$(MAKE) -C doc
	$(MAKE) -C doc/web release

release: distclean releasecheck
	$(MAKE) dist sign upload homepage tag register changelog deb

tag:
	git tag upstream/$(VERSION)
	git push --tags origin upstream/$(VERSION)

register:
	@echo "Register at Python Package Index..."
	$(PYTHON) setup.py register

releasecheck:
	git checkout master
	$(MAKE) check test
# test console output (behaves differently than redirected output)
	$(MAKE) test PYTESTOPTS="-s" TESTS=tests/test_dosage.py
	@if egrep -i "xx\.|xxxx|\.xx" doc/changelog.txt > /dev/null; then \
	  echo "Could not release: edit doc/changelog.txt release date"; false; \
	fi
	@if [ ! -f ../$(ARCHIVE_WIN32) ]; then \
	  echo "Missing WIN32 distribution archive at ../$(ARCHIVE_WIN32)"; \
	  false; \
	fi
#	$(PYTHON) setup.py check --restructuredtext
	git checkout debian
	@if ! head -1 debian/changelog | grep "$(VERSION)" > /dev/null; then \
	  echo "Could not release: update debian/changelog version"; false; \
	fi
	@if head -1 debian/changelog | grep UNRELEASED >/dev/null; then \
	  echo "Could not release: set debian/changelog release name"; false; \
	fi
	git checkout master

# The check programs used here are mostly local scripts on my private system.
# So for other developers there is no need to execute this target.
check:
	check-copyright
	check-py-encoding patoolib tests
	check-pofiles -v
	py-tabdaddy
	py-unittest2-compat tests/
	$(MAKE) doccheck

doccheck:
	py-check-docstrings --force \
	  dosagelib/*.py \
	  dosage \
	  scripts \
	  *.py

pyflakes:
	pyflakes dosage dosagelib scripts tests doc/web

count:
	@sloccount dosage dosagelib/*.py

clean:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete
	rm -rf build dist

distclean: clean
	rm -rf $(APPNAME).egg-info $(APPNAME).prof test.sh Comics
	rm -f _$(APPNAME)_configdata.py MANIFEST

localbuild:
	$(PYTHON) setup.py build

test:	localbuild
	env LANG=en_US.utf-8 http_proxy="" $(PYTHON) -m pytest $(PYTESTOPTS) $(TESTOPTS) $(TESTS)

testall:	localbuild
	env LANG=en_UR.utf-8 http_proxy="" TESTALL=1 $(PYTHON) -m pytest $(PYTESTOPTS) $(TESTOPTS) $(TESTS)

deb:
# Build an official .deb package; only useful for Debian maintainers.
# To build a local .deb package, use:
# $ sudo apt-get build-dep dosage; apt-get source dosage; cd dosage-*; debuild binary
	[ -f $(DEBORIGFILE) ] || cp dist/$(ARCHIVE_SOURCE) $(DEBORIGFILE)
	sed -i -e 's/VERSION_$(APPNAME):=.*/VERSION_$(APPNAME):=$(VERSION)/' $(DEBUILDDIR)/$(APPNAME).mak
	[ -d $(DEBPACKAGEDIR) ] || (cd $(DEBUILDDIR); \
	  patool extract $(DEBORIGFILE); \
	  cd $(CURDIR); \
	  git checkout debian; \
	  cp -r debian $(DEBPACKAGEDIR); \
	  rm -f $(DEBPACKAGEDIR)/debian/.gitignore; \
	  git checkout master)
	$(MAKE) -C $(DEBUILDDIR) $(APPNAME)_clean $(APPNAME)

update-copyright:
# update-copyright is a local tool which updates the copyright year for each
# modified file.
	update-copyright --holder="$(MAINTAINER)"

update-comics:
# update all scripted comic plugins (takes ca. one hour on my computer)
	scripts/generate_json.sh
	scripts/update_plugins.sh


changelog:
# github-changelog is a local tool which parses the changelog and automatically
# closes issues mentioned in the changelog entries.
	github-changelog $(DRYRUN) $(GITUSER) $(GITREPO) doc/changelog.txt

.PHONY: update-copyright deb test clean distclean count pyflakes changelog
.PHONY: doccheck check releasecheck release dist chmod localbuild sign
.PHONY: register tag homepage
