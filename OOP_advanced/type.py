#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 下午11:28
# @Author  : Zhang_xq
# @File    : type.py
# @Software: PyCharm


class A(object):
    pass


class Hello(A):
    def hello(self, name='world'):
        print('hello, %s' % name)


def fn(self, name='world'):  # 先定义函数
    print('hello, %s' % name)


hello1 = type('hello1', (object,), dict(hello1=fn))  # 创建class
s = hello1()
print(s.hello1())


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class Mylist(list, metaclass=ListMetaclass):
    pass


L = Mylist()
L.add(1)
print(L)


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s' % (self.__class__.name, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
