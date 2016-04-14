#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func1(a, b, f):
    return f(a) + f(b)


print func1(1, 2, abs)


def fucmap(x):
    return x * x


print map(fucmap, [1, 2, 3, 4])

L = [100, 9, 8, 1, 2, 3, 4, 5, 6]
print L
print map(str, L)


def add(a, b):
    return a + b


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
print reduce(add, L)


# return true or false
def is_odd(a):
    return a % 2 == 1


print filter(is_odd, L)

print sorted(L)


def lazy_fuc(a):
    def sum():
        b = 0
        for i in range(a):
            b += i

        return b

    return sum


ff = lazy_fuc(10)
print ff
print ff()


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print f1()
print f2()
print f3()

#
print map(lambda x: x * x, L)
f = lambda x: x * x
print f

funabs = abs
print funabs.__name__


# decorator
def log(func):
    def wrapper(*args, **kw):
        print 'call %s:' % func.__name__
        return func(*args, **kw)

    return wrapper


@log
def now():
    print '2016/4/15'


now()





