#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 上午1:53
# @Author  : Zhang_xq
# @File    : @property.py
# @Software: PyCharm


# class Student(object):
#     def get_score(self):
#         return self.score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('The score must be integer!')
#         if value < 0 or value > 100:
#             raise ValueError('Score must between 0-100!')
#         else:
#             self.score = value

class Student(object):
    """Student"""

    # __slots__ = ('score')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError
        if value < 0 or value > 100:
            raise ValueError
        self._score = value


s = Student()
s.score = 76
print(s.score)


# s.score = 9999


# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self.height * self.width


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
