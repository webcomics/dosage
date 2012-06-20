# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
"""
Automated webcomic downloader. Dosage traverses webcomic websites in
order to download each strip of the comic. The intended use is for
mirroring the strips locally for ease of viewing; redistribution of the
downloaded strips may violate copyright, and is not advisable unless you
have communicated with all of the relevant copyright holders, described
your intentions, and received permission to distribute.

The primary dosage interface is currently the 'mainline' script, which
is just a thin wrapper that invokes L{dosage.mainline}. Comic modules
for each webcomic are located in L{dosage.modules}; most of these make
use of the helper base classes and mixins in L{dosage.modules.helpers},
thus making their individual implementations trivial.

@group Core modules: comic, events, output, progress, rss, util,
       version
@group Interface modules: mainline
@group Comic modules: modules

@sort: modules.helpers

@author: U{Dosage development team <dosage@lists.slipgate.za.net>}
@requires: Python 2.3+
@see: U{The dosage webpage <http://slipgate.za.net/dosage>}
@see: U{The dosage Trac site <http://trac.slipgate.za.net/dosage>}

@newfield contributor: Contributor, Contributors (Alphabetical Order)
@contributor: U{Jonathan Jacobs <mailto:korpse@slipgate.za.net>}
@contributor: U{Tristan Seligmann <mailto:mithrandi@mithrandi.za.net>}

@var __license__: The license governing the use and distribution of
    dosage.
"""
__docformat__ = 'epytext en'
import sys
if not (hasattr(sys, 'version_info') or
        sys.version_info < (2, 5, 0, 'final', 0)):
    raise SystemExit("This program requires Python 2.5 or later.")

