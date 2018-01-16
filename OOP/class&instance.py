#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 16:11
# @Author  : Zhang_xq
# @File    : class&instance.py
# @Software: PyCharm


class Friend(object):
    """学生"""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Friend('Bart Fuckman', 72)
lisa = Friend('Lisa Simpson', 96)

bart.print_score()
print(bart.get_grade())
print(lisa.get_grade())

bart.fuck = 27
print(bart.fuck)
