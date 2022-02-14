# Dosage

[![Tests](https://github.com/webcomics/dosage/actions/workflows/test.yml/badge.svg)](https://github.com/webcomics/dosage/actions/workflows/test.yml)
[![Code Climate](https://codeclimate.com/github/webcomics/dosage/badges/gpa.svg)](https://codeclimate.com/github/webcomics/dosage)
[![codecov](https://codecov.io/gh/webcomics/dosage/branch/master/graph/badge.svg)](https://codecov.io/gh/webcomics/dosage)
![Maintenance](https://img.shields.io/maintenance/yes/2022.svg)
![License](https://img.shields.io/github/license/webcomics/dosage)

Dosage is designed to keep a local copy of specific webcomics and other
picture-based content such as Picture of the Day sites. With the dosage
commandline script you can get the latest strip of a webcomic, or catch-up to
the last strip downloaded, or download a strip for a particular date/index (if
the webcomic's site layout allows this).

Multiple webcomics can be downloaded in parallel, making the update of comic
strips faster.

Dosage is licensed under the [MIT license](COPYING)

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

### Adult content

Some comics contain adult content and require age confirmation. These comics
can only be downloaded by using the `--adult` option, which confirms that you
are old enough to view them.

## Installation

### Dependencies

Since dosage is written in [Python](http://www.python.org/), a Python
installation is required: Dosage needs at least Python 3.7. Dosage requires
some Python modules from PyPI, so installation with `pip` is recommended.

### Using the Windows binary

Windows users can download a complete binary (including Python) from the
[release page].

[release page]: https://github.com/webcomics/dosage/releases/latest

### Install with pipx

The simplest way to install and upgrade dosage is with [pipx]. To install the
newest stable version with all optional features use:

    pipx install dosage[css,bash]

To install the newest development version, use:

    pipx install "dosage[css,bash] @ git+https://github.com/webcomics/dosage.git"

To upgrade such installations, just run:

    pipx upgrade dosage

### Installation for development

If you want to run dosage directly from the source code, you should install
it in "[editable]" mode, preferable in a [virtual environment]:

    pip install -e .[css,bash,dev]


After that, `dosage` should be available as a normal command.

[pipx]: https://github.com/pipxproject/pipx
[editable]: https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs
[virtual environment]: https://docs.python.org/3/library/venv.html

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

Dosage has unit tests to ensure code quality. GitHub Actions are used for
continuous build and test integration. See the badges at the top of this page
for the current status.
