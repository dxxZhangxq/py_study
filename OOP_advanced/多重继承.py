#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 上午2:23
# @Author  : Zhang_xq
# @File    : 多重继承.py
# @Software: PyCharm


class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    pass


class Flyable(object):
    pass


# 各种动物
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Flyable):
    pass


class Ostrich(Bird, Runnable):
    pass
