import tempfile
import shutil
from itertools import izip
from unittest import TestCase
from dosagelib import scraper


class _ComicTester(TestCase):
    """Basic comic test class."""
    scraperclass=None

    def test_comic(self):
        # Test a scraper. It must be able to traverse backward for
        # at least 5 pages from the start, and find strip images
        # on at least 4 pages.
        module = self.scraperclass()
        num = empty = 0
        for n, comics in izip(xrange(5), module):
            if len(comics) == 0:
                empty += 1
            for comic in comics:
                self.save(comic)
            num += 1
        self.assertTrue(num >= 4, 'Traversal failed after %d strips.' % num)
        self.assertTrue(empty <= 1, 'Failed to find images on %d pages.' % empty)

    def save(self, comic):
        # create a temporary directory
        tmpdir = tempfile.mkdtemp()
        try:
            filename, saved = comic.save(tmpdir)
            self.assertTrue(saved, 'Could not save comic %s to %s' % (comic, tmpdir))
        finally:
            shutil.rmtree(tmpdir)


def generate_comic_testers():
    """For each comic scraper, create a test class.
    This currently generates over 4000 test classes (one for each comic),
    so this takes a while."""
    for s in scraper.items():
        name = 'Test'+s.__name__
        globals()[name] = type(name,
            (_ComicTester,),
            dict(scraperclass=s)
        )

generate_comic_testers()
