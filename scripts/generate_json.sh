#!/bin/sh
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher
set -e
set -u

d=$(dirname $0)
if [ $# -ge 1 ]; then
  list="$*"
else
  list="arcamax comicfury comicgenesis creators gocomics keenspot webcomicfactory comicskingdom"
fi
for script in $list; do
  echo "Executing ${script}.py"
  python3 "${d}/${script}.py"
done
