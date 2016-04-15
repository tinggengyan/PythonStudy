#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

__author__ = 'Steve yan'


def test():
    args = sys.argv
    if len(args) == 1:
        print "hello world", args
    elif len(args) == 2:
        print "hello %s!", args[1]
    else:
        print 'too many arguments'


if __name__ == '__main__':
    test()


# private method

def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

