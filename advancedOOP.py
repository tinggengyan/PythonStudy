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


class Student5(object):
    def __init__(self, name):
        self.name = name
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __str__(self):
        return 'Student5 ' + self.name

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration();
        return self.a  # 返回下一个值

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


s5 = Student5('steve')
print s5

for b in s5:
    print b

print s5[9]