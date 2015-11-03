# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015 Tobias Gruetzmacher
"""
Define basic configuration data like version or application name.
"""

from __future__ import print_function
from . import __version__, AppName

App = AppName + u' ' + __version__

Maintainer = u'Tobias Gruetzmacher'
MaintainerEmail = u'tobias-dosage@23.gs'
Url = u'http://dosage.rocks/'
SupportUrl = u'https://github.com/webcomics/dosage/issues'
UserAgent = u"Mozilla/5.0 (compatible; %s/%s; +%s)" % (AppName, __version__, Url)
Copyright = u"""Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
Copyright (C) 2012-2014 Bastian Kleineidam
Copyright (C) 2015 Tobias Gruetzmacher
"""
Freeware = AppName + u""" comes with ABSOLUTELY NO WARRANTY!
This is free software, and you are welcome to redistribute it
under certain conditions. Look at the file `COPYING' within this
distribution."""
VoteUrl = "http://gaecounter.appspot.com/"
