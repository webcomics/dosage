from re import compile, IGNORECASE, MULTILINE

from ..helpers import _BasicScraper



class _VGCats(_BasicScraper):
    latestUrl = 'http://www.vgcats.com/comics/'
    imageSearch = compile(r'<img src="(images/\d{6}\..+?)"')
    prevSearch = compile(r'<a href="(\?strip_id=\d+)"><img src="back.gif" border="0"')
    help = 'Index format: n (unpadded)'

    @property
    def imageUrl(self):
        return self.latestUrl + '?strip_id=%s'



class Super(_VGCats):
    name = 'VGCats/Super'
    latestUrl = 'http://www.vgcats.com/super/'



class Adventure(_VGCats):
    name = 'VGCats/Adventure'
    latestUrl = 'http://www.vgcats.com/ffxi/'



class ViiviJaWagner(_BasicScraper):
    latestUrl = 'http://www.hs.fi/viivijawagner/'
    imageUrl = 'http://www.hs.fi/viivijawagner/%s'
    imageSearch = compile(r'<img id="strip\d+"\s+src="([^"]+)"', IGNORECASE)
    prevSearch = compile(r'<a href="(.+?)"[^>]+?>\nEdellinen&nbsp;\n<img src="http://www.hs.fi/static/hs/img/viivitaakse.gif"', MULTILINE | IGNORECASE)
    help = 'Index format: shrugs!'
