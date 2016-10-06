# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import os
import threading
from six.moves import _thread
from six.moves.queue import Queue, Empty
from six.moves.urllib.parse import urlparse

from .output import out
from . import events, scraper


class ComicQueue(Queue):
    """The comic scraper job queue."""

    def join(self, timeout=None):
        """Blocks until all items in the Queue have been gotten and processed.

        The count of unfinished tasks goes up whenever an item is added to the
        queue. The count goes down whenever a consumer thread calls task_done()
        to indicate the item was retrieved and all work on it is complete.

        When the count of unfinished tasks drops to zero, join() unblocks.
        """
        self.all_tasks_done.acquire()
        try:
            while self.unfinished_tasks:
                self.all_tasks_done.wait(timeout)
        finally:
            self.all_tasks_done.release()

    def clear(self):
        """Remove all queue entries."""
        self.mutex.acquire()
        self.queue.clear()
        self.mutex.release()


# ensure threads download only from one host at a time
host_locks = {}


def get_hostname(url):
    """Get hostname from URL."""
    return list(urlparse(url))[1].lower()


lock = threading.Lock()


def get_host_lock(url):
    """Get lock object for given URL host."""
    hostname = get_hostname(url)
    return host_locks.setdefault(hostname, threading.Lock())


class ComicGetter(threading.Thread):
    """Get all strips of a comic in a thread."""

    def __init__(self, options):
        """Store options."""
        super(ComicGetter, self).__init__()
        self.options = options
        self.origname = self.name
        self.stopped = False
        self.errors = 0

    def run(self):
        """Process from queue until it is empty."""
        try:
            while not self.stopped:
                scraperobj = jobs.get(False)
                self.name = scraperobj.name
                try:
                    self.getStrips(scraperobj)
                finally:
                    jobs.task_done()
                    self.name = self.origname
        except Empty:
            pass
        except KeyboardInterrupt:
            _thread.interrupt_main()

    def getStrips(self, scraperobj):
        """Download comic strips."""
        with lock:
            host_lock = get_host_lock(scraperobj.url)
        with host_lock:
            self._getStrips(scraperobj)

    def _getStrips(self, scraperobj):
        """Get all strips from a scraper."""
        if self.options.all or self.options.cont:
            numstrips = None
        elif self.options.numstrips:
            numstrips = self.options.numstrips
        else:
            # get current strip
            numstrips = 1
        try:
            if scraperobj.isComplete(self.options.basepath):
                out.info(u"All comics are already downloaded.")
                return 0
            for strip in scraperobj.getStrips(numstrips):
                skipped = self.saveComicStrip(strip)
                if skipped and self.options.cont:
                    # stop when retrieval skipped an image for one comic strip
                    out.info(u"Stop retrieval because image file already exists")
                    break
                if self.stopped:
                    break
            if self.options.all and not (self.errors or self.options.dry_run or
                                         self.options.cont or
                                         scraperobj.indexes):
                scraperobj.setComplete(self.options.basepath)
        except Exception as msg:
            out.exception(msg)
            self.errors += 1

    def saveComicStrip(self, strip):
        """Save a comic strip which can consist of multiple images."""
        allskipped = True
        for image in strip.getImages():
            try:
                if self.options.dry_run:
                    filename, saved = "", False
                else:
                    filename, saved = image.save(self.options.basepath)
                if saved:
                    allskipped = False
                if self.stopped:
                    break
            except Exception as msg:
                out.exception('Could not save image at %s to %s: %r' % (image.referrer, image.filename, msg))
                self.errors += 1
        return allskipped

    def stop(self):
        """Mark this thread as stopped."""
        self.stopped = True


jobs = ComicQueue()
threads = []


def getComics(options):
    """Retrieve comics."""
    if options.handler:
        for name in set(options.handler):
            events.addHandler(name, options.basepath, options.baseurl, options.allowdownscale)
    events.getHandler().start()
    errors = 0
    try:
        for scraperobj in getScrapers(options.comic, options.basepath,
                                      options.adult, options.multimatch):
            jobs.put(scraperobj)
        # start threads
        num_threads = min(options.parallel, jobs.qsize())
        for i in range(num_threads):
            t = ComicGetter(options)
            threads.append(t)
            t.start()
        # wait for threads to finish
        jobs.join(1)
        for t in threads:
            errors += t.errors
    except ValueError as msg:
        out.exception(msg)
        errors += 1
    except KeyboardInterrupt:
        finish()
    finally:
        events.getHandler().end()
    return errors


def finish():
    """Print warning about interrupt and empty the job queue."""
    out.warn("Interrupted!")
    for t in threads:
        t.stop()
    jobs.clear()
    out.warn("Waiting for download threads to finish.")


def getScrapers(comics, basepath=None, adult=True, multiple_allowed=False, listing=False):
    """Get scraper objects for the given comics."""
    if '@' in comics:
        # only scrapers whose directory already exists
        if len(comics) > 1:
            out.warn(u"using '@' as comic name ignores all other specified comics.")
        for comic in get_existing_comics(basepath, adult, listing):
            yield comic
    else:
        # get only selected comic scrapers
        # store them in a set to eliminate duplicates
        scrapers = set()
        for comic in comics:
            # Helpful when using shell completion to pick comics to get
            comic = comic.rstrip(os.path.sep)
            if basepath and comic.startswith(basepath):
                # make the following command work:
                # find Comics -type d | xargs -n1 -P10 dosage -b Comics
                comic = comic[len(basepath):].lstrip(os.sep)
            if ':' in comic:
                name, index = comic.split(':', 1)
                indexes = index.split(',')
            else:
                name = comic
                indexes = None
            found_scrapers = scraper.find_scrapers(name, multiple_allowed=multiple_allowed)
            for scraperobj in found_scrapers:
                if shouldRunScraper(scraperobj, adult, listing):
                    # FIXME: Find a better way to work with indexes
                    scraperobj.indexes = indexes
                    if scraperobj not in scrapers:
                        scrapers.add(scraperobj)
                        yield scraperobj


def get_existing_comics(basepath=None, adult=True, listing=False):
    for scraperobj in scraper.get_scrapers(include_removed=True):
        dirname = scraperobj.get_download_dir(basepath)
        if os.path.isdir(dirname):
            if shouldRunScraper(scraperobj, adult, listing):
                yield scraperobj


def shouldRunScraper(scraperobj, adult=True, listing=False):
    if listing:
        return True
    if not adult and scraperobj.adult:
        warn_adult(scraperobj)
        return False
    reasons = scraperobj.getDisabledReasons()
    if reasons:
        warn_disabled(scraperobj, reasons)
        return False
    return True


def warn_adult(scraperobj):
    """Print warning about adult content."""
    out.warn(u"skipping adult comic %s; use the --adult option to confirm your age" % scraperobj.name)


def warn_disabled(scraperobj, reasons):
    """Print warning about disabled comic modules."""
    out.warn(u"Skipping comic %s: %s" % (scraperobj.name, ' '.join(reasons.values())))
