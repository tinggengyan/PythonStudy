#!/usr/bin/env python
# -*- coding: utf-8 -*-

# call method
print abs(-100)
print cmp(100, 90)
print int('192')
print float('192.19')
print unicode(100)
print bool(1)
print bool(0)


# define a method
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


# call the method
print my_abs(-9)


# empty method
def empty_method():
    pass


empty_method()

import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print move(1, 2, 3, 45)
x, y = move(1, 2, 3, 45)
print x, y


def power(v, z=2):
    return v * v + z


print power(9)


def calc(numbers):
    sums = 0
    for n in numbers:
        sums = sums + n * n
    return sums


print calc({1, 2, 3})


def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw


person('steve', 17)
person('steve', 17, city='shanghai')
person('steve', 17, city='shanghai', job=90)
