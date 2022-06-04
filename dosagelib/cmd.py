# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
import argparse
import os
import platform

from platformdirs import PlatformDirs

from . import events, configuration, singleton, director
from . import AppName, __version__
from .output import out
from .scraper import scrapers as scrapercache
from .util import internal_error, strlimit


class ArgumentParser(argparse.ArgumentParser):
    """Custom argument parser."""

    def print_help(self, file=None):
        """Paginate help message on TTYs."""
        with out.pager():
            out.info(self.format_help())


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


def setup_options():
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
    parser.add_argument('-b', '--basepath', action='store', default='Comics',
        metavar='PATH',
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
    parser.add_argument('comic', nargs='*',
        help='comic module name (including case insensitive substrings)')
    try:
        import argcomplete
        argcomplete.autocomplete(parser)
    except ImportError:
        pass
    return parser


def display_version(verbose):
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
        result, value = check_update()
        if result:
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
        else:
            if value is None:
                value = 'invalid update file syntax'
            text = ('An error occured while checking for an '
                    'update of %(app)s: %(error)s.')
            attrs = {'error': value, 'app': AppName}
            print(text % attrs)
    return 0


def set_output_info(options):
    """Set global output level and timestamp option."""
    out.level = 0
    out.level += options.verbose
    out.timestamps = options.timestamps


def display_help(options):
    """Print help for comic strips."""
    errors = 0
    try:
        for scraperobj in director.getScrapers(options.comic, options.basepath, listing=True):
            errors += display_comic_help(scraperobj)
    except ValueError as msg:
        out.exception(msg)
        return 2
    return errors


def display_comic_help(scraperobj):
    """Print help for a comic."""
    orig_context = out.context
    out.context = scraperobj.name
    try:
        out.info('URL: {}'.format(scraperobj.url))
        out.info('Language: {}'.format(scraperobj.language()))
        if scraperobj.adult:
            out.info(u"Adult comic, use option --adult to fetch.")
        disabled = scraperobj.getDisabledReasons()
        if disabled:
            out.info(u"Disabled: " + " ".join(disabled.values()))
        if scraperobj.help:
            for line in scraperobj.help.splitlines():
                out.info(line)
        return 0
    except ValueError as msg:
        out.exception(msg)
        return 1
    finally:
        out.context = orig_context


def vote_comics(options):
    """Vote for comics."""
    errors = 0
    try:
        for scraperobj in director.getScrapers(options.comic, options.basepath,
                options.adult):
            errors += vote_comic(scraperobj)
    except ValueError as msg:
        out.exception(msg)
        errors += 1
    return errors


def vote_comic(scraperobj):
    """Vote for given comic scraper."""
    errors = 0
    orig_context = out.context
    out.context = scraperobj.name
    try:
        scraperobj.vote()
        out.info(u'Vote submitted.')
    except Exception as msg:
        out.exception(msg)
        errors += 1
    finally:
        out.context = orig_context
    return errors


def run(options):
    """Execute comic commands."""
    set_output_info(options)
    scrapercache.adddir(user_plugin_path)
    # ensure only one instance of dosage is running
    if not options.allow_multiple:
        singleton.SingleInstance()
    if options.version:
        return display_version(options.verbose)
    if options.list:
        return do_list()
    if options.singlelist or options.list_all:
        return do_list(column_list=False, verbose=options.verbose,
                       listall=options.list_all)
    # after this a list of comic strips is needed
    if not options.comic:
        out.warn(u'No comics specified, bailing out!')
        return 1
    if options.modulehelp:
        return display_help(options)
    if options.vote:
        return vote_comics(options)
    return director.getComics(options)


def do_list(column_list=True, verbose=False, listall=False):
    """List available comics."""
    with out.pager():
        out.info(u'Available comic scrapers:')
        out.info(u'Comics tagged with [{}] require age confirmation'
            ' with the --adult option.'.format(TAG_ADULT))
        out.info(u'Non-english comics are tagged with [%s].' % TAG_LANG)
        scrapers = sorted(scrapercache.all(listall),
                          key=lambda s: s.name.lower())
        if column_list:
            num, disabled = do_column_list(scrapers)
        else:
            num, disabled = do_single_list(scrapers, verbose=verbose)
        out.info(u'%d supported comics.' % num)
        if disabled:
            out.info('')
            out.info(u'Some comics are disabled, they are tagged with'
                ' [{}:REASON], where REASON is one of:'.format(TAG_DISABLED))
            for k in disabled:
                out.info(u'  %-10s %s' % (k, disabled[k]))
    return 0


def do_single_list(scrapers, verbose=False):
    """Get list of scraper names, one per line."""
    disabled = {}
    for scraperobj in scrapers:
        if verbose:
            display_comic_help(scraperobj)
        else:
            out.info(get_tagged_scraper_name(scraperobj, reasons=disabled))
    return len(scrapers) + 1, disabled


def do_column_list(scrapers):
    """Get list of scraper names with multiple names per line."""
    disabled = {}
    width = out.width
    # limit name length so at least two columns are there
    limit = (width // 2) - 8
    names = [get_tagged_scraper_name(scraperobj, limit=limit, reasons=disabled)
             for scraperobj in scrapers]
    num = len(names)
    maxlen = max(len(name) for name in names)
    names_per_line = max(width // (maxlen + 1), 1)
    while names:
        out.info(u''.join(name.ljust(maxlen) for name in
                 names[:names_per_line]))
        del names[:names_per_line]
    return num, disabled


TAG_ADULT = "adult"
TAG_LANG = "lang"
TAG_DISABLED = "dis"


def get_tagged_scraper_name(scraperobj, limit=None, reasons=None):
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
    if tags:
        suffix = " [" + ", ".join(tags) + "]"
    else:
        suffix = ""
    name = scraperobj.name
    if limit is not None:
        name = strlimit(name, limit)
    return name + suffix


def main(args=None):
    """Parse options and execute commands."""
    try:
        options = setup_options().parse_args(args=args)
        options.basepath = os.path.expanduser(options.basepath)
        return run(options)
    except KeyboardInterrupt:
        print("Aborted.")
        return 1
    except Exception:
        internal_error()
        return 2
