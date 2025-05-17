# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# PYTHON_ARGCOMPLETE_OK
from __future__ import annotations

import argparse
import contextlib
import importlib
import logging
import os
import platform
from collections.abc import Iterable

from platformdirs import PlatformDirs
from rich import columns, console, table, text

from . import AppName, __version__, configuration, director, events, output, singleton
from .scraper import scrapers as scrapercache
from .util import internal_error

logger = logging.getLogger(__name__)


class ArgumentParser(argparse.ArgumentParser):
    """Custom argument parser."""

    def print_help(self, file=None) -> None:
        """Paginate help message on TTYs."""
        with self.console.pager():
            self.console.print(self.format_help())


# Making our config roaming seems sensible
platformdirs = PlatformDirs(appname=AppName, appauthor=False, roaming=True, opinion=True)
user_plugin_path = platformdirs.user_data_path / 'plugins'


ExtraHelp = f"""\
EXAMPLES
List available comics:
  dosage -l

Get the latest comic of for example CalvinAndHobbes and save it in the "Comics"
directory:
  dosage CalvinAndHobbes

If you already have downloaded several comics and want to get the latest
strips of all of them:
  dosage --continue @

User plugin directory: {user_plugin_path}
"""


def setup_options() -> ArgumentParser:
    """Construct option parser.
    @return: new option parser
    @rtype argparse.ArgumentParser
    """
    parser = ArgumentParser(
        description="A comic downloader and archiver.",
        epilog=ExtraHelp,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-v', '--verbose', action='count', default=0,
        help='provides verbose output, use multiple times for more verbosity')
    parser.add_argument('-n', '--numstrips', action='store', type=int, default=0,
        help='traverse and retrieve the given number of comic strips;'
        ' use --all to retrieve all comic strips')
    parser.add_argument('-a', '--all', action='store_true',
        help='traverse and retrieve all comic strips')
    parser.add_argument('-c', '--continue', action='store_true', dest='cont',
        help='traverse and retrieve comic strips until an existing one is found')
    basepath_opt = parser.add_argument('-b', '--basepath', action='store',
        default='Comics', metavar='PATH',
        help='set the path to create invidivual comic directories in, default is Comics')
    parser.add_argument('--baseurl', action='store', metavar='PATH',
        help='the base URL of your comics directory (for RSS, HTML, etc.);'
        ' this should correspond to --base-path')
    parser.add_argument('-l', '--list', action='store_true',
        help='list available comic modules')
    parser.add_argument('--singlelist', action='store_true',
        help='list available comic modules in a single column list')
    parser.add_argument('--version', action='store_true',
        help='display the version number')
    parser.add_argument('--vote', action='store_true',
        help='vote for the selected comics')
    parser.add_argument('-m', '--modulehelp', action='store_true',
        help='display help for comic modules')
    parser.add_argument('-t', '--timestamps', action='store_true',
        help='print timestamps for all output at any info level')
    parser.add_argument('-o', '--output', action='append', dest='handler',
        choices=events.getHandlerNames(),
        help='sets output handlers for downloaded comics')
    parser.add_argument('--no-downscale', action='store_false',
        dest='allowdownscale',
        help='prevent downscaling when using html or rss handler')
    parser.add_argument('-p', '--parallel', action='store', type=int, default=1,
        help='fetch comics in parallel. Specify the number of connections')
    parser.add_argument('--adult', action='store_true',
        help='confirms that you are old enough to view adult content')
    parser.add_argument('--allow-multiple', action='store_true',
        help='allows multiple instances to run at the same time.'
        ' Use if you know what you are doing.')
    # used for development testing prev/next matching
    parser.add_argument('--dry-run', action='store_true',
        help=argparse.SUPPRESS)
    # List all comic modules, even those normally suppressed, because they
    # are not "real" (moved & removed)
    parser.add_argument('--list-all', action='store_true',
        help=argparse.SUPPRESS)
    comic_arg = parser.add_argument('comic', nargs='*',
        help='comic module name (including case insensitive substrings)')
    comic_arg.completer = scraper_completion
    with contextlib.suppress(ImportError):
        completers = importlib.import_module('argcomplete.completers')
        basepath_opt.completer = completers.DirectoriesCompleter()
        importlib.import_module('argcomplete').autocomplete(parser)
    return parser


def scraper_completion(**kwargs) -> Iterable[str]:
    """Completion helper for argcomplete."""
    scrapercache.adddir(user_plugin_path)
    return (comic.name for comic in scrapercache.all())


def display_version(verbose: bool) -> None:
    """Display application name, version, copyright and license."""
    print(configuration.App)
    print("Using Python {} ({}) on {}".format(platform.python_version(),
        platform.python_implementation(), platform.platform()))
    print(configuration.Copyright)
    print(configuration.Freeware)
    print("For support see", configuration.SupportUrl)
    if verbose:
        # search for updates
        from .updater import check_update
        try:
            value = check_update()
            if value:
                version, url = value
                if url is None:
                    # current version is newer than online version
                    text = ('Detected local or development version %(currentversion)s. '
                            'Available version of %(app)s is %(version)s.')
                else:
                    # display update link
                    text = ('A new version %(version)s of %(app)s is '
                            'available at %(url)s.')
                attrs = {'version': version, 'app': AppName,
                    'url': url, 'currentversion': __version__}
                print(text % attrs)
        except (IOError, KeyError) as err:
            print(f'An error occured while checking for an update of {AppName}: {err!r}')


def display_help(options) -> None:
    """Print help for comic strips."""
    for scraperobj in director.getScrapers(options.comic, options.basepath, listing=True):
        display_comic_help(scraperobj)


def display_comic_help(scraperobj) -> None:
    """Print help for a comic."""
    context = {"context": scraperobj.name}
    logger.info('URL: %s', scraperobj.url, extra=context)
    logger.info('Language: %s', scraperobj.language(), extra=context)
    if scraperobj.adult:
        logger.info("Adult comic, use option --adult to fetch.", extra=context)
    disabled = scraperobj.getDisabledReasons()
    if disabled:
        logger.info("Disabled: %s", " ".join(disabled.values()), extra=context)
    if scraperobj.help:
        logger.info(scraperobj.help, extra=context)


def vote_comics(options) -> int:
    """Vote for comics."""
    errors = 0
    for scraperobj in director.getScrapers(options.comic, options.basepath,
            options.adult):
        errors += vote_comic(scraperobj)
    return errors


def vote_comic(scraperobj) -> int:
    """Vote for given comic scraper."""
    context = {"context": scraperobj.name}
    try:
        scraperobj.vote()
        logger.info('Vote submitted.', extra=context)
    except Exception as msg:
        logger.exception(msg, extra=context)  # noqa: G200
        return 1
    return 0


def run(console: console.Console, options) -> int:
    """Execute comic commands."""
    err = 0
    output.console_logging(console, options.verbose, options.timestamps)
    scrapercache.adddir(user_plugin_path)
    # ensure only one instance of dosage is running
    if not options.allow_multiple:
        singleton.SingleInstance()

    if options.version:
        display_version(options.verbose)
    elif options.list:
        do_list(console)
    elif options.singlelist or options.list_all:
        do_list(console, column_list=False, verbose=options.verbose,
            listall=options.list_all)
    else:
        # after this a list of comic strips is needed
        if not options.comic:
            logger.warning('No comics specified, bailing out!')
            return 1

        if options.modulehelp:
            display_help(options)
        elif options.vote:
            err = vote_comics(options)
        else:
            err = director.getComics(options)
    return err


def do_list(console: console.Console, column_list=True, verbose=False, listall=False) -> None:
    """List available comics."""
    with console.pager():
        logger.info('Available comic scrapers:')
        logger.info('Comics tagged with [%s] require age confirmation'
            ' with the --adult option.', TAG_ADULT)
        logger.info('Non-english comics are tagged with [%s].', TAG_LANG)
        scrapers = sorted(scrapercache.all(listall),
                          key=lambda s: s.name.lower())
        if column_list:
            num, disabled = do_column_list(console, scrapers)
        else:
            num, disabled = do_single_list(console, scrapers, verbose=verbose)
        logger.info('%d supported comics.', num)
        if disabled:
            logger.info('')
            logger.info('Some comics are disabled, they are tagged with'
                ' [%s:REASON], where REASON is one of:', TAG_DISABLED)
            for k in disabled:
                logger.info('  %-10s %s', k, disabled[k])


def do_single_list(console: console.Console, scrapers, verbose=False):
    """Get list of scraper names, one per line."""
    disabled = {}
    for scraperobj in scrapers:
        if verbose:
            display_comic_help(scraperobj)
        else:
            tagged = get_tagged_scraper(scraperobj, reasons=disabled)
            console.print(text.Text(' '.join(filter(None, tagged))))
    return len(scrapers), disabled


def do_column_list(console: console.Console, scrapers):
    """Get list of scraper names with multiple names per line."""
    disabled = {}
    tagged_names = [get_tagged_scraper(scraperobj, reasons=disabled)
             for scraperobj in scrapers]
    lengths = sorted(len(tagged[0]) + len(tagged[1]) for tagged in tagged_names)
    upper_length = lengths[int(len(lengths) * 0.97) - 1]
    expectedcols = console.width // upper_length
    maxwidth = (console.width // expectedcols) - 3
    logger.debug("Calculated column widths: max: %i, upper: %i, width: %i",
        lengths[-1], upper_length, maxwidth)
    elements = (tagged_to_table(tagged, maxwidth) for tagged in tagged_names)
    console.print(columns.Columns(elements, equal=True, expand=True))
    return len(tagged_names), disabled


TAG_ADULT = "adult"
TAG_LANG = "lang"
TAG_DISABLED = "dis"


def get_tagged_scraper(scraperobj, reasons: dict[str, str] = None) -> tuple[str, str]:
    """Get comic scraper name."""
    tags = []
    if scraperobj.adult:
        tags.append(TAG_ADULT)
    if scraperobj.lang != "en":
        tags.append("%s:%s" % (TAG_LANG, scraperobj.lang))
    disabled = scraperobj.getDisabledReasons()
    if disabled and reasons is not None:
        reasons.update(disabled)
    for reason in disabled:
        tags.append("%s:%s" % (TAG_DISABLED, reason))

    return scraperobj.name, "[" + ", ".join(tags) + "]" if tags else ""


def tagged_to_table(tagged: tuple[str, str], limit: int) -> table.Table:
    output = table.Table.grid(padding=(0, 1))
    name, tags = tagged
    output.add_column(max_width=limit - len(tags), overflow="ellipsis")
    if tags:
        output.add_column()
        output.add_row(name, text.Text(tags))
    else:
        output.add_row(name)
    return output


def main(args=None):
    """Parse options and execute commands."""
    try:
        console = output.setup_console()
        argparser = setup_options()
        argparser.console = console
        options = argparser.parse_args(args=args)
        options.basepath = os.path.expanduser(options.basepath)
        return run(console, options)
    except KeyboardInterrupt:
        print("Aborted.")
        return 1
    except Exception:
        internal_error()
        return 2
