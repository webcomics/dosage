#!/bin/sh
# Install PIL in Travis CI environment for Python 2.x builds.
set -e
set -u

if python -c 'import sys; sys.exit(0 if sys.hexversion<0x03000000 else 1)'; then
  pip install --allow-external PIL --allow-unverified PIL PIL
fi
