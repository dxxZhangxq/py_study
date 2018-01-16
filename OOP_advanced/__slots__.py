#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 上午1:28
# @Author  : Zhang_xq
# @File    : __slots__.py
# @Software: PyCharm
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Xi Jinping'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(66)
print(s.age)

s2 = Student()


# s2.set_age(25)  # 给一个实例绑定的方法，对另一个实例并没有卵用


def set_score(self, score):
    self.score = score
    return self.score


Student.set_score = set_score
s.set_score(26)


class Student1(object):
    __slots__ = ('name', 'age')


s = Student1()
s.name = 'Xi Jinping'
s.age = 67
# s.fuck = 987954
# print(s.fuck)
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
