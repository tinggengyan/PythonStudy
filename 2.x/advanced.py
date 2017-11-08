#!/usr/bin/env python
# -*- coding: utf-8 -*-

L = []
n = 1
while n < 100:
    L.append(n)
    n += 1
print n
print L

# the first 3
print L[0:3]
print L[1:4]
print L[:9]
print L[-10:]

# iterator
for k in L:
    print k

print range(1, 10)
for yy in range(1, 10):
    print yy

print [x * x for x in range(1, 10)]

import os

dirs = [d for d in os.listdir('.')]
print dirs
print [s.upper() for s in dirs]

# generator
g = (x * x for x in range(10, 20))
for gg in g:
    print gg


def fib(max):
    nn, a, b = 0, 0, 1
    while nn < max:
        yield b
        a, b = b, a + b
        nn += 1


for f in fib(6):
    print f
