#!/bin/sh -e
# Copyright (C) 2012-2013 Bastian Kleineidam
set -u

mincomics=100
d=$(dirname $0)

for script in creators gocomics drunkduck universal keenspot smackjeeves arcamax; do
  target="${d}/../dosagelib/plugins/${script}.py"
  echo "Upating $target"
  "${d}/removeafter.py" "$target" "# DO NOT REMOVE"
  "${d}/${script}.py" $mincomics >> "$target"
done
