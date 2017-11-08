# -*-coding:utf8-*-

import os
import re
import sys
import urllib
import urllib2

import requests
from bs4 import BeautifulSoup
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')

cookie = {
    "Cookie": ""}
url = 'http://m.weibo.cn/index/feed?format=cards&next_cursor=3967532723727284&page=1'
html = requests.get(url, cookies=cookie).content
selector = etree.HTML(html)
pageNum = selector.xpath('//script[@language]/text()')

print pageNum

print html
