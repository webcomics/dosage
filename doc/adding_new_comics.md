# Adding a comic to Dosage

To add a new comic to a local dosage installation, drop a python file into
Dosage's "user plugin directory" - If you don't know where that is, run `dosage
--help`, the directory will be shown at the end.

Here is a complete example which is explained in detail below. Dosage provides
different base classes for parsing comic pages, but this tutorial only covers
the modern `ParserScraper` base class, which uses an HTML parser (LXML/libxml)
to find  on each pages's DOM.

```python
from ..scraper import ParserScraper

class SuperDuperComic(ParserScraper):
    url = 'https://superdupercomic.com/'
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[d:class("comicpane")]//img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: n (unpadded)'
```

Let's look at each line in detail.

```python
class SuperDuperComic(ParserScraper):
```

All comic plugin classes inherit from `ParserScraper`. The class name
(`SuperDuperComic` in our example) must be unique, regardless of upper/lower
characters. The user finds comics with this class name, so be sure to select
something descriptive and easy to remember.

```python
url = 'https://superdupercomic.com/'
```

The URL must display the latest comic picture. This is where the comic image
search will start. See below for some special cases.

```python
stripUrl = url + 'comics/%s'
```

This defines how a comic strip URL looks like. In our example, all comic strip
URLs look like `https://superdupercomic.com/comics/NNN` where NNN is the
increasing comic number.

```python
firstStripUrl = stripUrl % '1'
```

This tells Dosage what the earliest comic strip URL looks like. Dosage stops
searching for more comics when it is encounterd. In our example comic numbering
starts with `1`, so the oldest comic URL is
`https://superdupercomic.com/comics/1`

```python
imageSearch = '//div[d:class("comicpane")]//img'
```

Each comic page URL has one or more comic strip images. The `imageSearch`
defines an [XPath](https://quickref.me/xpath) expression to find the comic
strip image inside each page. Most of the time you can use your browser's
console (Open with `F12`) to experiment on the real page. Dosage adds a custom
XPath function (`d:class`) to make it easier to match HTML classes.

```python
prevSearch = '//a[@rel="prev"]'
```

To search for more comics, Dosage has to look for the previous comic URL. This
property defines an XPath expression to find a link to the previous comic page.

```python
help = 'Index format: n (unpadded)'
```

Since the user can search comics from a given start point, the help can
describe how the comic is numbered. Running `dosage superdupercomic:100` would
start getting comics from number 100 and earlier.

## Contribute a module to dosage

If you don't know how to use git and/or setup a Python development environment,
that's fine! You can [create an
issue](https://github.com/webcomics/dosage/issues/new) on GitHub and paste the
source of your new module into it and a Dosage developer will take care of
integrating the module into Dosage.

Otherwise, integrate your new comic module into in one of the `*.py` files in
the dosagelib/plugins module.

The files in dosagelib/plugins and the classes inside those files are sorted
alphabetically. Add your comic to the appropriate filename. For example if the
comic name is "Super duper comic", the new class should be added to
dosagelib/plugins/s.py.
