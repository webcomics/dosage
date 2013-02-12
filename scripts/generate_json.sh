#!/bin/sh
set -e
set -u

d=$(dirname $0)
for script in creators gocomics drunkduck keenspot smackjeeves arcamax; do
  echo "Executing ${script}.py"
  "${d}/${script}.py"
done
