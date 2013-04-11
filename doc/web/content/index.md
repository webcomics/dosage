title: a comic strip downloader and archiver
description: a comic strip downloader and archiver
---
Introduction
-------------
Dosage is designed to keep a local copy of specific webcomics
and other picture-based content such as Picture of the Day sites.
With the dosage commandline script you can get the latest strip of
a webcomic, or catch-up to the last strip downloaded, or download a
strip for a particular date/index (if the webcomic's site layout
allows this).

Notice
-------
This software is in no way intended to publically "broadcast" comic strips,
it is purely for personal use. Please be aware that by making downloaded
strips publically available (without the explicit permission of the author)
you may be infringing upon various copyrights.

Additionally, Dosage respects the robots.txt exclusion protocol.
This makes sure no content is accessed in an automatic way without consent
by the publishers.

If you are a publisher of comics and want Dosage to access your files,
add the following entry to your robotst.txt file:

```
User-agent: Dosage
Allow: *
```

Adult content
--------------
Some comics contain adult content and require age confirmation.
These comics can only be downloaded by using the --adult option,
which confirms that you are old enough to view them.</p>

Usage
------
List [available comics](comic-index.html) (ca. 3000 at the moment):

```bash
$ dosage --list
```

Get the latest comic of for example CalvinAndHobbes and save it in the "Comics"
directory:

```bash
$ dosage CalvinAndHobbes
```

If you already have downloaded several comics and want to get the latest
strip of all of them:

```bash
$ dosage @
```

To help others find good [comics](comic-index.html), you can vote for your
favourite ones:

```bash
$ dosage --vote @
```

For advanced options and features execute `dosage --help` or look at the
[dosage(1) manual page](dosage.1.html).

Note that the old commandline program `maintool` has been renamed to
`dosage`.

Dependencies
-------------
[Python version 2.7](http://www.python.org/) or higher

Also the [python-requests module](http://docs.python-requests.org/en/latest/) must be installed

Installation
-------------
You can invoke Dosage directly from the source code as 
`./dosage`. Alternatively,
you can install Dosage using python distutils by invoking
setup.py in the root of the distribution. For example:

```shell
python setup.py install
```

or if you do not have root permissions:

```shell
python setup.py install --home=$HOME
```

Another option is to use pip:

```shell
pip install dosage
```


Technical Description
----------------------
Dosage is written in Python and relies on regular expressions to
do most of the grunt work.

For each webcomic Dosage has a plugin module, found in the
`dosagelib/plugins` subdirectory. Each module is a subclass of
the `_BasicScraper` class and specifies where to download its comic images.
Some comic syndicates (ucomics for example) have a standard layout for all
comics. For such cases there are general base classes derived from
`_BasicScraper` which help define the plugins for all comics of this syndicate.

Extending Dosage
-----------------
In order to add a new webcomic, a new module class has to be created in
one of the *.py files in the `dosagelib/plugins` subdirectory.
Look at the existing module classes for examples.

Reporting Bugs
---------------
You can report bugs, patches or requests at the
[Github issue tracker](https://github.com/wummel/dosage/issues)

Dosage currently supports a large number of comics and that number
grows on a regular basis. If you feel that there are comics that
Dosage does not currently support but should support, please
feel free to request them.

Test suite status
------------------
Dosage has extensive unit tests to ensure the code quality.
[Travis CI](https://travis-ci.org/) is used for continuous build
and test integration.

[![Build Status](https://travis-ci.org/wummel/dosage.png)](https://travis-ci.org/wummel/dosage)

