# This Makefile is only used by developers.
PYVER:=2.7
PYTHON:=python$(PYVER)
VERSION:=$(shell $(PYTHON) setup.py --version)
ARCHIVE:=dosage-$(VERSION).tar.gz
PY_FILES_DIRS := dosage dosagelib tests *.py
PY2APPOPTS ?=
NOSETESTS:=$(shell which nosetests)
NUMPROCESSORS:=$(shell grep -c processor /proc/cpuinfo)
CHMODMINUSMINUS:=--
# which test modules to run
TESTS ?= tests/
# set test options, eg. to "--nologcapture"
TESTOPTS=

all:


.PHONY: chmod
chmod:
	-chmod -R a+rX,u+w,go-w $(CHMODMINUSMINUS) *
	find . -type d -exec chmod 755 {} \;

.PHONY: dist
dist:
	git archive --format=tar --prefix=dosage-$(VERSION)/ HEAD | gzip -9 > ../$(ARCHIVE)
	[ -f ../$(ARCHIVE).sha1 ] || sha1sum ../$(ARCHIVE) > ../$(ARCHIVE).sha1
	[ -f ../$(ARCHIVE).asc ] || gpg --detach-sign --armor ../$(ARCHIVE)

doc/dosage.1.html: doc/dosage.1
	man2html -r $< | tail -n +2 | sed 's/Time:.*//g' | sed 's@/:@/@g' > $@

.PHONY: release
release: distclean releasecheck dist
	git tag v$(VERSION)
#	@echo "Register at Python Package Index..."
#	$(PYTHON) setup.py register
#	freecode-submit < dosage.freecode


.PHONY: releasecheck
releasecheck: check test
	@if egrep -i "xx\.|xxxx|\.xx" doc/changelog.txt > /dev/null; then \
	  echo "Could not release: edit doc/changelog.txt release date"; false; \
	fi
#	@if ! grep "Version: $(VERSION)" dosage.freecode > /dev/null; then \
#	  echo "Could not release: edit dosage.freecode version"; false; \
#	fi

# The check programs used here are mostly local scripts on my private system.
# So for other developers there is no need to execute this target.
.PHONY: check
check:
	[ ! -d .svn ] || check-nosvneolstyle -v
	check-copyright
	check-pofiles -v
	py-tabdaddy
	py-unittest2-compat tests/

.PHONY: pyflakes
pyflakes:
	pyflakes $(PY_FILES_DIRS)

.PHONY: count
count:
	@sloccount dosage dosagelib | grep "Total Physical Source Lines of Code"

.PHONY: clean
clean:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete
	rm -rf build dist

PHONY: distclean
distclean: clean
	rm -rf build dist Dosage.egg-info
	rm -f _Dosage_configdata.py MANIFEST

.PHONY: test
test:
	$(PYTHON) $(NOSETESTS) -v --processes=$(NUMPROCESSORS) -m "^test_.*" $(TESTOPTS) $(TESTS)

.PHONY: deb
deb:
	git-buildpackage --git-export-dir=../build-area/ --git-upstream-branch=master --git-debian-branch=debian  --git-ignore-new

comics:
	./dosage -v @@ > comics.log 2>&1

.PHONY: update-copyright
update-copyright:
	update-copyright --holder="Bastian Kleineidam"
