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
Copyright = u"Copyright (C) 2004-2008 "+Author
HtmlCopyright = u"Copyright &copy; 2004-2008 "+HtmlAuthor
Url = configdata.url
SupportUrl = Url + u"/issues"
Email = configdata.author_email
UserAgent = u"Mozilla/5.0 (compatible; %s/%s; +%s)" % (AppName, Version, Url)
Freeware = AppName+u""" comes with ABSOLUTELY NO WARRANTY!
This is free software, and you are welcome to redistribute it
under certain conditions. Look at the file `LICENSE' within this
distribution."""

