# -*- coding: utf-8 -*-
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher
"""
Define basic configuration data like version or application name.
"""

from __future__ import absolute_import, division, print_function

from . import AppName, AppVersion

App = AppName + u' ' + AppVersion

Maintainer = u'Tobias Gruetzmacher'
MaintainerEmail = u'tobias-dosage@23.gs'
Url = u'http://dosage.rocks/'
SupportUrl = u'https://github.com/webcomics/dosage/issues'
UserAgent = u"Mozilla/5.0 (compatible; %s/%s; +%s)" % (AppName, AppVersion,
                                                       Url)
Copyright = u"""Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
Copyright (C) 2012-2014 Bastian Kleineidam
Copyright (C) 2015-2017 Tobias Gruetzmacher
"""
Freeware = AppName + u""" comes with ABSOLUTELY NO WARRANTY!
This is free software, and you are welcome to redistribute it
under certain conditions. Look at the file `COPYING' within this
distribution."""
VoteUrl = "http://gaecounter.appspot.com/"
