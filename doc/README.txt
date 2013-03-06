Dosage
=======

Dosage is a commandline comic downloader and archiver.

Introduction
-------------
Dosage is designed to keep a local copy of specific webcomics
and other picture-based content such as Picture of the Day sites.
With the dosage commandline script you can get the latest strip of
a webcomic, or catch-up to the last strip downloaded, or download a
strip for a particular date/index (if the webcomic's site layout
makes this possible).

Notice
-------
This software is in no way intended to publically "broadcast" comic strips,
it is purely for personal use. Please be aware that by making downloaded
strips publically available (without the explicit permission of the author)
you may be infringing upon various copyrights.

Additionally, Dosage respects the robots.txt exclusion protocol. This
makes sure no content is accessed in an automatic way without consent
by the publishers.

If you are a publisher of comics and want Dosage to access your files,
add the following entry to your robotst.txt file:

```
User-agent: dosage
Allow: *
```

Adult content
--------------
Some comics contain adult content and require age confirmation.
These comics can only be downloaded by using the --adult option,
which confirms that you are old enough to view them.

Usage
------
List available comics (ca. 3000 at the moment):

`$ dosage -l`

Get the latest comic of for example CalvinAndHobbes and save it in the "Comics"
directory:

`$ dosage CalvinAndHobbes`

If you already have downloaded several comics and want to get the latest
strip of all of them:

`$ dosage @`

On Unix, ``xargs`` can download several comic strips in parallel,
for example using up to 4 processes:

`$ cd Comics && find . -type d | xargs -n1 -P4 dosage -b . -v`

For advanced options and features execute `dosage -h` or look at the dosage
manual page.

Installation
-------------
The most convenient method is to use pip, which installs all dependencies
automatically:

`pip install dosage`

If you install Dosage from source, the `dosage` script can be run directly with
`./dosage`. Alternatively, you can install Dosage using python distutils by invoking
setup.py in the root of the distribution. For example:

`python setup.py install`

or if you do not have root permissions:

`python setup.py install --home=$HOME`

Dependencies
-------------
Python version 2.7 or higher, which can be downloaded
from http://www.python.org/

Also the python-requests module is used, which can be downloaded
from http://docs.python-requests.org/en/latest/

Technical Description
----------------------
Dosage is written in Python and relies on regular expressions to
do most of the grunt work.

For each comic Dosage has a plugin module, found in the "plugins"
subdirectory of the dosagelib directory. Each module is a subclass of
the _BasicComic class and specifies where to download its comic images.
Some comic syndicates (GoComics for example) have a standard layout for all
comics. For such cases a generator function creates all _BasicComic class
instances from a given list of comic strips.

Extending Dosage
-----------------
In order to add a new comic, a new module class has to be created in
one of the *.py files in the dosagelib/plugins subdirectory.
Look at the existing module classes for examples.

Reporting Bugs
---------------
You can report bugs, patches or requests at the Github issue tracker at
https://github.com/wummel/dosage/issues

Dosage currently supports a large number of comics and that number grows on
a regular basis. If you feel that there are comics that Dosage does not
currently support but should support, please feel free to request them.
