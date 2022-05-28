#!/bin/sh
if ! [ "$container" ]
then
    echo 'ERROR: Not running inside a container!'
    exit 1
fi
set -eu

HOME="/tmp/home"
mkdir -p "$HOME"
cd /work
pip install --no-warn-script-location --user pytest-cov PySocks
pip install --no-warn-script-location --user -e '.[css,dev]'

TESTALL=1 python3 -m py.test -v --cov=. --cov-report xml \
    --alluredir=allure-data \
    --tb=short -n10 --junitxml=junit.xml \
    tests/modules/check_comics.py || true

