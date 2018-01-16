#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 上午2:29
# @Author  : Zhang_xq
# @File    : 定制类.py
# @Software: PyCharm


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

        # __repr__ = __str__


print(Student('fuck'))
s = Student('haha')
print(s)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:  # 退出循环的条件
            raise StopIteration
        return self.a  # 返回下一个值

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


for n in Fib():
    print(n)
print(Fib()[5])


class Student2(object):
    def __init__(self):
        self.name = 'XJP'

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 25
        raise AttributeError


s1 = Student2()
print(s1.name)
print(s1.score)
print(s1.age())


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return 'my name is %s' % self.name

a = Student3('JZM')
print(a())
