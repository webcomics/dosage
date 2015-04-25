# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015 Tobias Gruetzmacher
"""
Define basic configuration data like version or application name.
"""

AppName = u'dosage'
Version = u'2.16' # Should be PEP 440 compatible
App = AppName + u' ' + Version
Maintainer = u'Tobias Gruetzmacher'
MaintainerEmail = u'tobias-dosage@23.gs'
Url = u'http://dosage.rocks/'
SupportUrl = u'https://github.com/webcomics/dosage/issues'
UserAgent = u"Mozilla/5.0 (compatible; %s/%s; +%s)" % (AppName, Version, Url)
Copyright = u"""Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
Copyright (C) 2012-2014 Bastian Kleineidam
Copyright (C) 2015 Tobias Gruetzmacher
"""
Freeware = AppName + u""" comes with ABSOLUTELY NO WARRANTY!
This is free software, and you are welcome to redistribute it
under certain conditions. Look at the file `COPYING' within this
distribution."""
VoteUrl = "http://gaecounter.appspot.com/"
