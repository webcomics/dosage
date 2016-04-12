# -*- coding: utf-8 -*-
from ..helpers import indirectStarter
from ..scraper import make_scraper
from .common import _WordPressScraper


def add(name, start):
    attrs = dict(
        name=name,
        url='http://hijinksensue.com/',
        latestSearch=start,
        starter=indirectStarter()
    )
    globals()[name] = make_scraper(name, _WordPressScraper, **attrs)


# all comics on HijiNKS ENSUE
for (name, starterXPath) in [
    ('HijinksEnsue', '//h4[text()="Read The Latest HijiNKS ENSUE"]/..//a'),
    ('HijinksEnsueClassic', '//h4[text()="Read HijiNKS ENSUE Classic"]/..//a[3]'),
    ('Faneurysm', '//h4[text()="Read The Latest FANEURYSM"]/..//a'),
    ('HijinksEnsueConvention', '//h4[text()="Latest Fancy Convention Sketches"]/..//a'),
    ('HijinksEnsuePhoto', '//h4[text()="Latest Fancy Photo Comic"]/..//a')
]:
    add(name, starterXPath)
