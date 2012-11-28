Dosage
=======

Dosage is a powerful webcomic downloader and archiver.

Introduction
-------------
Dosage is designed to keep a local copy of specific webcomics
and other picture-based content such as Picture of the Day sites.
With the dosage commandline script you can get the latest strip of
webcomic, or catch-up to the last strip downloaded, or download a
strip for a particular date/index (except if the webcomic's site layout
makes this impossible).

Notice
-------
This software is in no way intended to publically "broadcast" comic strips,
it is purely for personal use. Please be aware that by making downloaded
strips publically available (without the explicit permission of the author)
you may be infringing upon various copyrights.

Usage
------
List available comics (over 3500 at the moment):

`$ dosage -l`

Get the latest comic of for example CalvinAndHobbes and save it in the "Comics"
directory:

`$ dosage CalvinAndHobbes`

If you already have downloaded several comics and want to get the latest
strip of all of them:

`$ dosage @`

For advanced options and features execute `dosage -h` or look at the dosage
manual page.

Dependencies
-------------
Python version 2.7 or higher, which can be downloaded
from http://www.python.org/

Also the python-requests module must be installed, which can be downloaded
from http://docs.python-requests.org/en/latest/

Installation
-------------
You can invoke Dosage directly from the source code as "./dosage". Alternatively,
you can install Dosage using python distutils by invoking setup.py in
the root of the distribution. For example:

`python setup.py install`

or if you do not have root permissions:

`python setup.py install --home=$HOME`

Technical Description
----------------------
Dosage is written in Python and relies on regular expressions to
do most of the grunt work.

For each webcomic Dosage has a plugin module, found in the "plugins"
subdirectory of the dosagelib directory. Each module is a subclass of
the _BasicComic class and specifies where to download its comic images.
Some comic syndicates (ucomics for example) have a standard layout for all
comics. For such cases there are general base classes derived from _BasicComic
which help define the plugins for all comics of this syndicate.

Extending Dosage
-----------------
In order to add a new webcoming, a new module class has to be created in one of the
*.py files in the dosagelib/plugins subdirectory. Look at the existing
module classes for examples.

Reporting Bugs
---------------
You can report bugs, patches or requests at the Github issue tracker at
https://github.com/wummel/dosage/issues

Dosage currently supports a large number of comics and that number grows on
a regular basis. If you feel that there are comics that Dosage does not
currently support but should support, please feel free to request them.

