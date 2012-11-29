#!/bin/sh -e
# Copyright (C) 2012 Bastian Kleineidam
set -u
# generates a convenience test script from failed tests

script=test.sh

rm -f "$script"
echo "#!/bin/sh -e" > "$script"
egrep -v "^\. " testresults.txt | egrep "^F " | cut -b "3-" | awk '{ print "make test TESTOUTPUT=/dev/null TESTS=" $0; }' >> "$script"
chmod 755 "$script"

