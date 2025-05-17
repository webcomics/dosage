# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
"""
Define basic configuration data like version or application name.
"""
from . import AppName, __version__

App = f'{AppName} {__version__}'

Maintainer = 'Tobias Gruetzmacher'
MaintainerEmail = 'tobias-dosage@23.gs'
Url = 'https://dosage.rocks/'
SupportUrl = 'https://github.com/webcomics/dosage/issues'
UserAgent = f"Mozilla/5.0 (compatible; {AppName}/{__version__}; +{Url})"
Copyright = """Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
Copyright (C) 2012-2014 Bastian Kleineidam
Copyright (C) 2015-2025 Tobias Gruetzmacher
Copyright (C) 2019-2020 Daniel Ring
"""
Freeware = f"""{AppName} comes with ABSOLUTELY NO WARRANTY!
This is free software, and you are welcome to redistribute it
under certain conditions. Look at the file `COPYING' within this
distribution."""
VoteUrl = "https://buildbox.23.gs/count/"
