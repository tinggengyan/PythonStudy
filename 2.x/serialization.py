#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import json

d = dict(name='Bob', age=20, score=100)
# 序列化任意对象成str
print pickle.dumps(d)

# dump the content to the file
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# reload the content to the memory
ff = open('dump.txt', 'rb')
dd = pickle.load(ff)
ff.close()
print dd

# json
print json.dumps(d)


# advanced json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dit(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('steve', 20, 100)
print (json.dumps(s, default=student2dit))

print (json.dumps(s, default=lambda obj: obj.__dict__))
