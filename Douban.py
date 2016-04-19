#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
from bs4 import BeautifulSoup
import sys


class Douban(object):
    def __init__(self):
        self.fileHandle = open('doubanMoviesTop250.txt', 'w+')
        self.number = 1
        reload(sys)
        sys.setdefaultencoding('utf-8')

    def getTop250(self, start):
        url = 'https://movie.douban.com/top250?start=' + str(start) + '&filter='
        html = urllib2.urlopen(url)
        soup = BeautifulSoup(html)
        spanSet = soup.findAll('span', attrs={"class": "title"})
        for span in spanSet:
            imageName = span.string
            # get the chinese name
            if imageName.find('/') == -1:
                print imageName
                self.fileHandle.write(str(self.number) + ':' + imageName + "\n")
                self.number = self.number + 1
            else:
                print imageName
                self.fileHandle.write('英文名:' + imageName + "\n")

    def out(self):
        for i in range(10):
            self.getTop250(i * 25)


if __name__ == '__main__':
    douban = Douban()
    douban.out()
