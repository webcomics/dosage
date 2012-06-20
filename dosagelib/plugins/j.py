# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, MULTILINE

from ..helpers import _BasicScraper



class Jack(_BasicScraper):
    latestUrl = 'http://www.pholph.com/'
    imageUrl = 'http://www.pholph.com/strip.php?id=5&sid=%s'
    imageSearch = compile(r'<img src="(./artwork/.+?/Jack.+?)"')
    prevSearch = compile(r'\|<a href="(.+?)">Previous Strip</a>')
    help = 'Index format: n (unpadded)'



class JerkCity(_BasicScraper):
    latestUrl = 'http://www.jerkcity.com/'
    imageUrl = 'http://www.jerkcity.com/jerkcity%s'
    imageSearch = compile(r'"jerkcity.+?">.+?"(/jerkcity.+?)"')
    prevSearch = compile(r'"(jerkcity.+?)">.+?"/jerkcity.+?"')
    help = 'Index format: unknown'



class JoeAndMonkey(_BasicScraper):
    latestUrl = 'http://www.joeandmonkey.com/'
    imageUrl = 'http://www.joeandmonkey.com/%s'
    imageSearch = compile(r'"(/comic/[^"]+)"')
    prevSearch = compile(r"<a href='(/\d+)'>Previous")
    help = 'Index format: nnn'



class JoyOfTech(_BasicScraper):
    latestUrl = 'http://www.geekculture.com/joyoftech/index.html'
    imageUrl = 'http://www.geekculture.com/joyoftech/joyarchives/%s.html'
    imageSearch = compile(r'<img src="(joyimages/.+?|../joyimages/.+?)" alt="The Joy')
    prevSearch = compile(r'<a href="((?:joyarchives/)?\w+\.\w{3,4})">(?:<font[^>]*>)?<img[^>]*><br>[\s\n]*Previous Joy', MULTILINE)
    help = 'Index format: nnn'
