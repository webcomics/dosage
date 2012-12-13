# This Makefile is only used by developers.
PYVER:=2.7
PYTHON:=python$(PYVER)
VERSION:=$(shell $(PYTHON) setup.py --version)
ARCHIVE:=dosage-$(VERSION).tar.gz
PY_FILES_DIRS := dosage dosagelib scripts tests
PY2APPOPTS ?=
# Default pytest options:
# Do not use parallel testing with -n: it makes some tests fail since
# some web servers have limits on the number of parallel connections.
# Also note that using -n silently swallows test creation exceptions like
# import errors.
PYTESTOPTS?=--resultlog=testresults.txt --tb=short
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
	@echo "Register at Python Package Index..."
	$(PYTHON) setup.py register
	freecode-submit < dosage.freecode


releasecheck: check
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
	@sloccount $(PY_FILES_DIRS) | grep "Total Physical Source Lines of Code"

clean:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete
	rm -rf build dist

distclean: clean
	rm -rf build dist Dosage.egg-info dosage.prof test.sh testresults.txt
	rm -f _Dosage_configdata.py MANIFEST

localbuild:
	$(PYTHON) setup.py build

test:	localbuild
	env LANG=en_US.utf-8 http_proxy="" $(PYTHON) -m pytest $(PYTESTOPTS) $(TESTOPTS) $(TESTS)

deb:
	git-buildpackage --git-upstream-branch=master --git-debian-branch=debian  --git-ignore-new

update-copyright:
	update-copyright --holder="Bastian Kleineidam"

.PHONY: update-copyright deb test clean distclean count pyflakes
.PHONY: doccheck check releasecheck release dist chmod localbuild
