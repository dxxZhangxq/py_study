#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 16:06
# @Author  : Zhang_xq
# @File    : oop.py
# @Software: PyCharm


class Student(object):
    """学生"""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart Simpson', 66)
lisa = Student('Lisa Simpson', 99)
bart.print_score()
lisa.print_score()
