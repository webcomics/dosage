# -*- coding: utf-8 -*-
from ..helpers import indirectStarter
from ..scraper import make_scraper
from .common import _WordPressScraper


def add(name, url, starter=None):
    attrs = dict(
        name=name,
        url=url
    )
    if starter:
        attrs['starter'] = starter
    globals()[name] = make_scraper(name, _WordPressScraper, **attrs)


# all comics on HijiNKS ENSUE
for (name, starterXPath) in [
    ('HijinksEnsue', '//h4[text()="Read The Latest HijiNKS ENSUE"]/..//a'),
    ('HijinksEnsueClassic', '//h4[text()="Read HijiNKS ENSUE Classic"]/..//a[3]'),
    ('Faneurysm', '//h4[text()="Read The Latest FANEURYSM"]/..//a'),
    ('HijinksEnsueConvention', '//h4[text()="Latest Fancy Convention Sketches"]/..//a'),
    ('HijinksEnsuePhoto', '//h4[text()="Latest Fancy Photo Comic"]/..//a')
]:
    add(name, 'http://hijinksensue.com/', starter=indirectStarter('http://hijinksensue.com/', starterXPath))

# all comics on flowerlarkstudios
for (name, linkNumber) in [
    ('Ashes', 1),
    ('Eryl', 3),
    # this is a duplicate as it was under this name in previous versions of dosage
    ('DarkWings', 3),
    ('Laiyu', 5),
    ('NoMoreSavePoints', 7),
    ('EasilyAmused', 9)
]:
    add(name, 'http://www.flowerlarkstudios.com/',
        starter=indirectStarter('http://www.flowerlarkstudios.com/',
                                '(//div[@id="sidebar-left"]//a)[' + str(linkNumber) + ']'))
