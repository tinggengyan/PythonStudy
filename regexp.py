# -*- coding: utf-8 -*-
import re

match = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
if match:
    print 'ok'
else:
    print 'failed'

split = re.split(r'[\s,]+', 'a ,  ,,,b    c   d')
print split

re_match = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

for m in re_match.groups():
    print m
