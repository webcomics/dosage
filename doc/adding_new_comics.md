How to add a new comic to Dosage
=================================

To add a new comic, add a new class in one of the *.py files
in the dosagelib/plugins module.

The files in dosagelib/plugin and the classes inside those files are
sorted alphabetically. Add your comic to the appropriate filename.
For example if the comic name is "Super duper comic", the new class
should be added to dosagelib/plugins/s.py.

Here is a complete example which is explained in detail below.

```
class SuperDuperComic(_BasicScraper):
    url = 'http://superdupercomic.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%scomicimg/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomic/\d+)' % rurl, after="prev"))
    help = 'Index format: n (unpadded)'
```

Let's look at each line in detail.

```class SuperDuperComic(_BasicScraper):```

All comic plugin classes inherit from ``_BasicScraper``.
The classname (``SuperDuperComic`` in our example) must be unique,
regardless of upper/lower characters.
The user finds comics with this classname, so be sure to select
something descriptive and easy to remember.

```url = 'http://superdupercomic.com/'```

The URL must display the latest comic picture. This is where the
comic image search will start. See below for some special cases.

```rurl = escape(url)```

This defines a variable ``rurl`` which is used in the search patterns
below. It properly escapes all regular expression special characters
like dots or question marks.

```stripUrl = url + 'comic/%s'```

This defines how a comic strip URL looks like. In our example, all
comic strip URLs look like ``http://superdupercomic.com/comics/NNN``
where NNN is the increasing comic number.

```firstStripUrl = stripUrl % '1'```

This tells Dosage what the earliest comic strip URL looks like. Dosage
stops searching for more comics when it is encounterd. In our example
comic numbering starts with ``1``, so the oldest comic URL is
``http://superdupercomic.com/comics/1``

```imageSearch = compile(tagre("img", "src", r'(%simg/[^"]+)' % rurl))```

Each comic page URL has one or more comic strip images. The imageSearch
pattern must match those images in the HTML content of the page URL.
To make it easy to match HTML tags, the ``tagre()`` function is
helpful. The first parameter is the tag name, the second the attribute
name and the third the attribute value. So in our example the given
pattern whould match a tag like
``<img src="http://superdupercomic.com/img/comic1.jpg" />``` .

```prevSearch = compile(tagre("a", "href", r'(%scomic/\d+)' % rurl, after="prev"))```

To search for more comics, Dosage has to look for the previous comic URL.
The ``after=`` value in ``tagre()`` matches anything between the
attribute value and the end of the tag.
So this pattern assumes each comic page URL has a link to the previous
comic, for example ``http://superdupercomic.com/comic/100`` has a
link ``<a href="http://superdupercomic.com/comic/99" class="prev">``.

``help = 'Index format: n (unpadded)'``

Since the user can search comics from a given start point, the help
must describe how the comic is numbered. Running
``dosage superdupercomic:100`` would start getting comics from number
100 and earlier.
