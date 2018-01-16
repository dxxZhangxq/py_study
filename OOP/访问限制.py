#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 16:23
# @Author  : Zhang_xq
# @File    : 访问限制.py
# @Software: PyCharm


class People(object):
    """学生"""

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        """print student's score"""
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        """grade"""
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        """访问__name"""
        return self.__name

    def get_score(self):
        """访问__score"""
        return self.__score

    # def set_score(self, score):
    #     """设置score"""
    #     self.__score = score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError


bart = People('Bart Fool', 99)
print(bart.get_name())

bart.__score = 23
print(bart.__score)
bart.print_score()
# 创建了一个新的变量叫__score, 原来那个改为_People__score

# bart.set_score(163)
# 这里会报错
# print(bart.get_score())

bart.set_score(23)
bart.print_score()


# print(bart._Student1__score, bart._Student1__name)
# 不要这样访问变量 贼不讲究


# 练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender not in ('male', 'female'):
            raise ValueError
        else:
            self.__gender = gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')