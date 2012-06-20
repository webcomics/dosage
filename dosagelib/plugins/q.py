from re import compile

from ..helpers import _BasicScraper



class QuestionableContent(_BasicScraper):
    latestUrl = 'http://www.questionablecontent.net/'
    imageUrl = 'http://www.questionablecontent.net/view.php?comic=%s'
    imageSearch = compile(r'/(comics/\d+\.png)"')
    prevSearch = compile(r'<a href="(view.php\?comic=\d+)">Previous')
    help = 'Index format: n (unpadded)'



class Qwantz(_BasicScraper):
    latestUrl = 'http://www.qwantz.com/index.php'
    imageUrl = 'http://www.qwantz.com/index.php?comic=%s'
    imageSearch = compile(r'<img src="(http://www.qwantz.com/comics/.+?)" class="comic"')
    prevSearch = compile(r'"><a href="(.+?)">&larr; previous</a>')
    help = 'Index format: n'
