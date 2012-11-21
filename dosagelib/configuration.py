# Copyright (C) 2012 Bastian Kleineidam
"""
Define basic configuration data like version or application name.
"""
import _Dosage_configdata as configdata

Version = configdata.version
ReleaseDate = configdata.release_date
AppName = configdata.name
App = AppName+u" "+Version
Author = configdata.author
HtmlAuthor = Author.replace(u' ', u'&nbsp;')
Maintainer = configdata.maintainer
HtmlMaintainer = Maintainer.replace(u' ', u'&nbsp;')
Copyright = u"Copyright (C) 2004-2008 " + \
  (u",".join(Author.split(",")[:2]))+u"  (C) 2012 "+Maintainer
HtmlCopyright = u"Copyright &copy; 2004-2008 " + \
  (u",".join(HtmlAuthor.split(",")[:2]))+u" &copy; 2012 "+HtmlMaintainer
Url = configdata.url
SupportUrl = Url + u"/issues"
Email = configdata.maintainer_email
UserAgent = u"Mozilla/5.0 (compatible; %s/%s; +%s)" % (AppName, Version, Url)
Freeware = AppName+u""" comes with ABSOLUTELY NO WARRANTY!
This is free software, and you are welcome to redistribute it
under certain conditions. Look at the file `LICENSE' within this
distribution."""

