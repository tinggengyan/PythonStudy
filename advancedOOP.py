# -*- coding: utf-8 -*-
class Student(object):
    pass


s = Student()
s.name = 'steve'
print s.name


# 定义一个方法
def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s, Student)  # 给实例绑定一个方法
s.set_age(25)
print s.age

# 对于新的实例是无效的
s2 = Student()


# s2.set_age (26)
# print s2.age


# 给所有的实例都绑新的方法是可以绑定到class上的。
def set_score(self, score):
    self.score = score


Student.set_score = MethodType(set_score, None, Student)
s.set_score(100)
print s.score
s2.set_score(120)
print s2.score


class Student2(object):
    __slots__ = ('name', 'age')


ss = Student2()
ss.name = 'steve'
ss.age = 20
# ss.score = 100
print ss.name
print ss.age


class Studen3(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must be 0~100')
        self._score = value


s3 = Studen3()
s3.set_score(60)
print s3.get_score()


# s3.set_score(1000) error

class Student4(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self._score = value


s4 = Student4()
s4.score = 100
print  s4.score


