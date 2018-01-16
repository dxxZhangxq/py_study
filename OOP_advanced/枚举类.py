#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 下午2:43
# @Author  : Zhang_xq
# @File    : 枚举类.py
# @Software: PyCharm
from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 1
    Mon = 2
    Tue = 3
    Wed = 4
    Thr = 5
    Fri = 6
    Sat = 7


day1 = Weekday.Mon
print(day1)
# for name, member in Weekday.__members__.values():
# print(name, member, member.value)
# 这个循环根本跑不起来
print(type(Weekday))
print(type(Weekday.__members__.values()))


# 练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
print(bart.gender)
