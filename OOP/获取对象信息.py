#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-12 下午11:48
# @Author  : Zhang_xq
# @File    : 获取对象信息.py
# @Software: PyCharm
import types

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))


def fn():
    pass


# print(type(fn) == types.FunctionType)
# should us isinstance
print(dir('233'))


class MyDog(object):
    def __len__(self):
        return 120


dog = MyDog()
print(len(dog))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(getattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 29)
# print(obj.y)
print(getattr(obj, 'y'))
