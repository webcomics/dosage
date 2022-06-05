# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
import os
import re
import threading
import _thread
from queue import Queue, Empty
from typing import Collection, Dict
from urllib.parse import urlparse

from .output import out
from .scraper import scrapers as scrapercache
from . import events


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
host_locks: Dict[str, threading.Lock] = {}


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

    def __init__(self, options, jobs):
        """Store options."""
        super(ComicGetter, self).__init__()
        self.options = options
        self.jobs = jobs
        self.origname = self.name
        self.stopped = False
        self.errors = 0

    def run(self):
        """Process from queue until it is empty."""
        try:
            while not self.stopped:
                scraperobj = self.jobs.get(False)
                self.name = scraperobj.name
                try:
                    self.getStrips(scraperobj)
                finally:
                    self.jobs.task_done()
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
        if self.options.numstrips:
            numstrips = self.options.numstrips
        elif self.options.cont or self.options.all:
            numstrips = None
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
            if (self.options.all or
                self.options.cont) and not (self.errors or
                                            self.options.dry_run or
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
                out.exception('Could not save image at {} to {}: {!r}'.format(
                    image.referrer, image.filename, msg))
                self.errors += 1
        return allskipped

    def stop(self):
        """Mark this thread as stopped."""
        self.stopped = True


def getComics(options):
    """Retrieve comics."""
    threads = []
    jobs = ComicQueue()

    if options.handler:
        for name in set(options.handler):
            events.addHandler(name, options.basepath, options.baseurl, options.allowdownscale)
    events.getHandler().start()
    errors = 0
    try:
        for scraperobj in getScrapers(options.comic, options.basepath,
                options.adult):
            jobs.put(scraperobj)
        # start threads
        num_threads = min(options.parallel, jobs.qsize())
        for _i in range(num_threads):
            t = ComicGetter(options, jobs)
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
        out.warn("Interrupted! Waiting for download threads to finish.")
    finally:
        for t in threads:
            t.stop()
        jobs.clear()
        events.getHandler().end()
        events.clear_handlers()
    return errors


def getScrapers(comics: Collection[str], basepath: str, adult=True, listing=False):
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
        basere = re.compile(r'^' + re.escape(basepath) + r'[/\\]')
        for comic in comics:
            # Helpful when using shell completion to pick comics to get
            comic = comic.rstrip(os.path.sep)
            if basere.match(comic):
                # make the following command work:
                # find Comics -type d | xargs -n1 -P10 dosage -b Comics
                comic = comic[len(basepath) + 1:].lstrip(os.sep)
            if ':' in comic:
                name, index = comic.split(':', 1)
                indexes = index.split(',')
            else:
                name = comic
                indexes = None
            scraper = scrapercache.find(name)
            if shouldRunScraper(scraper, adult, listing):
                # FIXME: Find a better way to work with indexes
                scraper.indexes = indexes
                if scraper not in scrapers:
                    scrapers.add(scraper)
                    yield scraper


def get_existing_comics(basepath=None, adult=True, listing=False):
    for scraperobj in scrapercache.all(include_removed=True):
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
    out.warn(u"skipping adult comic {};"
        " use the --adult option to confirm your age".format(scraperobj.name))


def warn_disabled(scraperobj, reasons):
    """Print warning about disabled comic modules."""
    out.warn(u"Skipping comic {}: {}".format(
        scraperobj.name, ' '.join(reasons.values())))
