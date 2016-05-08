#!/usr/bin/env python
# -*- coding: utf-8 -*-

# open the file
try:
    f = open('README.MD', 'r')
    # read the content
    content = f.read()
    print content
finally:
    # close the file
    f.close()

# read the file by lines
with open("README.MD", 'r') as f:
    for line in f.readlines():
        print line.strip()

# open the file and decode the content with the encoding
f = open("README.MD", 'rb')
u = f.read().decode('gbk')
print u

import codecs

# auto decode the content encoding
with codecs.open("README.MD", 'r', 'gbk') as f:
    print f.read()

with open('testoutput.txt', 'w') as f:
    f.write("test output content")
    f.close()

