# -*-coding:utf8-*-

import os
import re
import sys
import urllib
import urllib2

import requests
from bs4 import BeautifulSoup
from lxml import etree
import time

reload(sys)
sys.setdefaultencoding('utf-8')

cookie = {
    "Cookie": "此处放入cookie"}
keyword = raw_input(u"请输入查询关键字")
fo = open("E:\\" + keyword + ".txt", "wb")

number = 1
for page in range(100):
    url = 'http://weibo.cn/search/mblog?hideSearchFrame=&keyword=' + keyword + '&page=' + str(page)
    html = requests.get(url, cookies=cookie).content
    selector = etree.HTML(html)
    content = selector.xpath('//span[@class="ctt"]')
    for each in content:
        text = each.xpath('string(.)')
        print text
        fo.write(str(number) + ":" + text)
        fo.write("\n")
        number += 1
time.sleep(1)
