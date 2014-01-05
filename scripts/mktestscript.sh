#!/bin/sh
# Copyright (C) 2012-2014 Bastian Kleineidam
set -e
set -u
# generates a convenience test script from failed tests
# since py.test has no way to rerun only the failed ones

script=test.sh

rm -f "$script"
echo "#!/bin/sh" > "$script"
echo "set -e" >> "$script"
egrep "^F " testresults.txt | cut -b "3-" | sort | awk '{ print "make testall PYTESTOPTS=--tb=short TESTS=" $0; }' >> "$script"
chmod 755 "$script"
