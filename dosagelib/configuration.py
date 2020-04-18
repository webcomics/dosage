# SPDX-License-Identifier: MIT
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
"""
Define basic configuration data like version or application name.
"""
from . import AppName, __version__

App = AppName + u' ' + __version__

Maintainer = u'Tobias Gruetzmacher'
MaintainerEmail = u'tobias-dosage@23.gs'
Url = u'https://dosage.rocks/'
SupportUrl = u'https://github.com/webcomics/dosage/issues'
UserAgent = u"Mozilla/5.0 (compatible; %s/%s; +%s)" % (AppName, __version__,
                                                       Url)
Copyright = u"""Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
Copyright (C) 2012-2014 Bastian Kleineidam
Copyright (C) 2015-2020 Tobias Gruetzmacher
Copyright (C) 2019-2020 Daniel Ring
"""
Freeware = AppName + u""" comes with ABSOLUTELY NO WARRANTY!
This is free software, and you are welcome to redistribute it
under certain conditions. Look at the file `COPYING' within this
distribution."""
VoteUrl = "https://buildbox.23.gs/count/"
