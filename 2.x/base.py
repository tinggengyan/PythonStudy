#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print absolute value of a integer
a = 100
if a > 100:
    print 'absolute bigger'
else:
    print 'absolute litter'

# string
print 'a string'
print 'string \"include" '
print "a string my name is steve' include ' "
# boolean

b = 100 > 10
print b
b1 = 10 < 1
print b1

if b and b1:
    print 'b and b1 =', b and b1
else:
    print 'b or b1 =', b or b1

print 'not b1', not b1

# variable
variable = 100
print 'now variable is ', variable, 'the type is ', type(variable)
variable = 'steve yan'
print 'now variable is ', variable, 'the type is ', type(variable)

# final variable does't exit in python
PI = 3.1415926
print PI

# charset
print ord('A')
print chr(97)
print u'中文'.encode('utf-8')

# format the output
print 'hello,%s,your score is %d' % ('steve', 100)

# list
classMates = ['yan', 'yang']
print classMates
print 'classMates\'s length', len(classMates)
print 'classMates first is ', classMates[0]
print 'the last one is ', classMates[-1]
print 'the last two is ', classMates[-2]
# insert
classMates.insert(1, 'hello')
# delete
classMates.pop(-1)
print classMates
print 'list\'s length is  ', len(classMates)
s = ['python', 'java', ['asp', 'php'], 'scheme']
print s[2]

# tuple can not change
teachers = ('A', 'B')
print teachers

for name in teachers:
    print name

# dict
scores = {'steve': 100, 'he': 90, 'she': 100}
print scores['he']
print 'steve' in scores
print scores.get('s')

classMates.append('steve')
classMates.append('steve')
setDemo = set(classMates)
print setDemo
setDemo.add('steve')
setDemo.add('steve')
print setDemo
setDemo.remove('steve')
print setDemo
