# This Makefile is only used by developers.
PYVER:=2.7
PYTHON:=python$(PYVER)
VERSION:=$(shell $(PYTHON) setup.py --version)
ARCHIVE:=dosage-$(VERSION).tar.gz
PY_FILES_DIRS := dosage dosagelib tests *.py
PY2APPOPTS ?=
NUMPROCESSORS:=$(shell grep -c processor /proc/cpuinfo)
MAXFAILEDTESTS:=10
# Pytest options:
# - stop after MAXFAILEDTESTS failed errors
# - use multiple processors
# - write test results in file
# - run all tests found in the "tests" subdirectory
PYTESTOPTS:=--maxfail=$(MAXFAILEDTESTS) -n $(NUMPROCESSORS) --resultlog=testresults.txt --tb=short
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
	git archive --format=tar --prefix=dosage-$(VERSION)/ HEAD | gzip -9 > ../$(ARCHIVE)
	[ -f ../$(ARCHIVE).sha1 ] || sha1sum ../$(ARCHIVE) > ../$(ARCHIVE).sha1
	[ -f ../$(ARCHIVE).asc ] || gpg --detach-sign --armor ../$(ARCHIVE)

doc/dosage.1.html: doc/dosage.1
	man2html -r $< | tail -n +2 | sed 's/Time:.*//g' | sed 's@/:@/@g' > $@

release: distclean releasecheck dist
	git tag v$(VERSION)
#	@echo "Register at Python Package Index..."
#	$(PYTHON) setup.py register
#	freecode-submit < dosage.freecode


releasecheck: check test
	@if egrep -i "xx\.|xxxx|\.xx" doc/changelog.txt > /dev/null; then \
	  echo "Could not release: edit doc/changelog.txt release date"; false; \
	fi
#	@if ! grep "Version: $(VERSION)" dosage.freecode > /dev/null; then \
#	  echo "Could not release: edit dosage.freecode version"; false; \
#	fi

# The check programs used here are mostly local scripts on my private system.
# So for other developers there is no need to execute this target.
check:
	[ ! -d .svn ] || check-nosvneolstyle -v
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
	  *.py

pyflakes:
	pyflakes $(PY_FILES_DIRS)

count:
	@sloccount dosage dosagelib | grep "Total Physical Source Lines of Code"

clean:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete
	rm -rf build dist

distclean: clean
	rm -rf build dist Dosage.egg-info
	rm -f _Dosage_configdata.py MANIFEST

localbuild:
	$(PYTHON) setup.py build

test:	localbuild
	$(PYTHON) -m pytest $(PYTESTOPTS) $(TESTOPTS) $(TESTS)

deb:
	git-buildpackage --git-export-dir=../build-area/ --git-upstream-branch=master --git-debian-branch=debian  --git-ignore-new

comics:
	./dosage -v @@ > comics.log 2>&1

update-copyright:
	update-copyright --holder="Bastian Kleineidam"

.PHONY: update-copyright comics deb test clean distclean count pyflakes
.PHONY: doccheck check releasecheck release dist chmod localbuild
