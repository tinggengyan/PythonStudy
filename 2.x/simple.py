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
if (len(sys.argv) >= 2):
    user_id = (int)(sys.argv[1])
else:
    user_id = (int)(raw_input(u"请输入user_id: "))

cookie = {
    "Cookie": "SINAGLOBAL=7412674727174.669.1446907386140; ULV=1460206518069:95:5:3:7918156561600.03.1460206518049:1460121985812; UOR=,,offlintab.firefoxchina.cn; SUHB=09P8wi8Neq2j5J; wb_publish_vip_2081490305=5; _s_tentry=login.sina.com.cn; Apache=7918156561600.03.1460206518049; SUS=SID-2081490305-1461401121-GZ-gzsna-fb1427862c3e12c6e8f933d56af1c8db; SUE=es%3D3bf4b0019c5b2f5cfe3ff06cbe60adf0%26ev%3Dv1%26es2%3De51b9c434772a6012836eff2f128ddc6%26rs0%3DJe7EyZz6mh%252BvlSAbERxW5pmDtwvWCM36gdL8oh6XYpzbxBEHOiMYaNmcS2QI7VWWu6tqpAQh2643LZ5Iy77BhN54FUKyZ9iXgAe1WP8Evz54XdVJFkWSZkmldz9mfVNoS8u8sRGvdE0l6Vz1U2H4ehjohKUQKo5ujjsT%252B%252BGmu3k%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1461401121%26et%3D1461487521%26d%3Dc909%26i%3Dc8db%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D2081490305%26name%3D15221318313%26nick%3D%25E7%2594%25A8%25E6%2588%25B72081490305%26fmp%3D%26lcp%3D2011-08-07%252015%253A20%253A48; ULOGIN_IMG=146115925223; YF-Ugrow-G0=3a02f95fa8b3c9dc73c74bc9f2ca4fc6; SUB=_2A256H0ZxDeRxGeRO41MV-S7PyzmIHXVZbTC5rDV8PUJbstBeLXb4kW9LHetCsknr9cwZ2GBomcUnuKgYDlbCaw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFKZ584vhlpFydZMA2uLf7_5JpX5o2p; ALF=1492921158; SSOLoginState=1461385159; YF-V5-G0=3d0866500b190395de868745b0875841; YF-Page-G0=602506db2d7072c030a3784f887e1d83; wvr=6"}
url = 'http://weibo.cn/u/%d?filter=1&page=1' % user_id

html = requests.get(url, cookies=cookie).content
selector = etree.HTML(html)
pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])

result = ""
urllist_set = set()
word_count = 1
image_count = 1

print u'爬虫准备就绪...'

for page in range(1, pageNum + 1):

    # 获取lxml页面
    url = 'http://weibo.cn/u/%d?filter=1&page=%d' % (user_id, page)
    lxml = requests.get(url, cookies=cookie).content

    # 文字爬取
    selector = etree.HTML(lxml)
    content = selector.xpath('//span[@class="ctt"]')
    for each in content:
        text = each.xpath('string(.)')
        if word_count >= 4:
            text = "%d :" % (word_count - 3) + text + "\n\n"
        else:
            text = text + "\n\n"
        result = result + text
        word_count += 1

    # 图片爬取
    soup = BeautifulSoup(lxml, "lxml")
    urllist = soup.find_all('a', href=re.compile(r'^http://weibo.cn/mblog/oripic', re.I))
    first = 0
    for imgurl in urllist:
        urllist_set.add(requests.get(imgurl['href'], cookies=cookie).url)
        image_count += 1

fo = open("E:\WorkSpace\PycharmProjects\%s" % user_id, "wb")
fo.write(result)
word_path = os.getcwd() + '/%d' % user_id
print u'文字微博爬取完毕'

link = ""
fo2 = open("E:\WorkSpace\PycharmProjects\%s_imageurls" % user_id, "wb")
for eachlink in urllist_set:
    link = link + eachlink + "\n"
fo2.write(link)
print u'图片链接爬取完毕'

if not urllist_set:
    print u'该页面中不存在图片'
else:
    # 下载图片,保存在当前目录的pythonimg文件夹下
    image_path = "E:\WorkSpace\PycharmProjects\weibo_image"
    if os.path.exists(image_path) is False:
        os.mkdir(image_path)
    x = 1
    for imgurl in urllist_set:
        temp = image_path + '/%s.jpg' % x
        print u'正在下载第%s张图片' % x
        try:
            urllib.urlretrieve(urllib2.urlopen(imgurl).geturl(), temp)
        except:
            print u"该图片下载失败:%s" % imgurl
        x += 1

print u'原创微博爬取完毕，共%d条，保存路径%s' % (word_count - 4, word_path)
print u'微博图片爬取完毕，共%d张，保存路径%s' % (image_count - 1, image_path)
