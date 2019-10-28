# Dosage

[![Build Status](https://travis-ci.org/webcomics/dosage.svg?branch=master)](https://travis-ci.org/webcomics/dosage)
[![Code Climate](https://codeclimate.com/github/webcomics/dosage/badges/gpa.svg)](https://codeclimate.com/github/webcomics/dosage)
[![codecov](https://codecov.io/gh/webcomics/dosage/branch/master/graph/badge.svg)](https://codecov.io/gh/webcomics/dosage)
[![Maintenance](https://img.shields.io/maintenance/yes/2019.svg)]()

Dosage is designed to keep a local copy of specific webcomics and other
picture-based content such as Picture of the Day sites. With the dosage
commandline script you can get the latest strip of a webcomic, or catch-up to
the last strip downloaded, or download a strip for a particular date/index (if
the webcomic's site layout allows this).

Multiple webcomics can be downloaded in parallel, making the update of comic
strips faster.

## Notice

This software is in no way intended to publically "broadcast" comic strips, it
is purely for personal use. Please be aware that by making downloaded strips
publically available (without the explicit permission of the author) you may be
infringing upon various copyrights.

Additionally, Dosage respects the robots.txt exclusion protocol. This makes
sure no content is accessed in an automatic way without consent by the
publishers.

In any case, you should support the authors of the comics you are downloading,
either by buying some of their products or even donating them some money since
they provide the comics you like and read.

If you are a publisher of comics and want Dosage to access your files,
add the following entry to your robots.txt file:

    User-agent: Dosage
    Allow: *

## Adult content

Some comics contain adult content and require age confirmation. These comics
can only be downloaded by using the `--adult` option, which confirms that you
are old enough to view them.

## Usage

List available comics (ca. 3000 at the moment):

    $ dosage --list

Get the latest comic of for example CalvinAndHobbes and save it in the "Comics"
directory:

    $ dosage CalvinAndHobbes

If you already have downloaded several comics and want to get the latest strip
of all of them:

    $ dosage @


To help others find good comics, you can vote for your favourite ones:

    $ dosage --vote @

For advanced options and features execute `dosage --help`.

## Dependencies

[Python](http://www.python.org/): for Python 2.x at least 2.7.0, for Python 3.x
at least Python 3.5. Dosage requires the following Python modules:

- colorama
- lxml
- requests
- six

For certain modules, you need the `cssselect` module, for bash argument
completion you need the `argcomplete` module.

## Installation

The easy way with pip:

    pip install --user dosage

You can invoke Dosage directly from the source code as `./dosage`.
Alternatively, you can install Dosage using setuptools by invoking `setup.py`
in the root of the distribution. For example:

    python setup.py install

or if you do not have root permissions:

    python setup.py install --home=$HOME

## Reporting Bugs

You can report bugs, patches or requests at the [GitHub issue
tracker](https://github.com/webcomics/dosage/issues) - Dosage currently
supports a large number of comics and that number grows on a regular basis. If
you feel that there are comics that Dosage does not currently support, but
should support, please feel free to request them.

## Extending Dosage

In order to add a new webcomic, a new module class has to be created in one of
the *.py files in the `dosagelib/plugins` subdirectory. Look at the
[documentation for adding modules](doc/adding_new_comics.md) and at
existing module classes for examples.

### Test suite status

Dosage has extensive unit tests to ensure the code quality.
[Travis-CI](https://travis-ci.org/) is used for continuous build and test
integration. See the badges at the top of this page for the current status.
