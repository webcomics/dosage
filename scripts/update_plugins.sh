#!/bin/sh
# Copyright (C) 2012-2014 Bastian Kleineidam
set -e
set -u

mincomics=100
d=$(dirname $0)

if [ $# -ge 1 ]; then
  list="$*"
else
  list="creators gocomics comicgenesis keenspot smackjeeves arcamax comicfury"
fi
for script in $list; do
  target="${d}/../dosagelib/plugins/${script}.py"
  echo "Upating $target"
  "${d}/removeafter.py" "$target" "# DO NOT REMOVE"
  "${d}/${script}.py" $mincomics "$target"
done
