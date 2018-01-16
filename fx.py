#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 15:54
# @Author  : Zhang_xq
# @File    : fx.py
# @Software: PyCharm

import math


def quadratic(a, b, c):
    """计算ax^2+bx+c=0的两个实根"""
    if not isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        raise TypeError('fuck off')
    delta = (b ** 2) - (4 * a * c)
    if 0 == a:
        return "error_0"
    if delta < 0:
        return "error_1"
    if delta >= 0:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return x1, x2


# 测试:

# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')


def power(x, n=2):
    """计算x^n, n的默认值为2"""
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def calc(*numbers):
    """计算x^2+(x-1)^2+...+1"""
    sum1 = 0
    for n in numbers:
        sum1 = sum1 + n ** 2
    return sum1


def product(*numbers):
    """计算乘积"""
    if len(numbers) == 0:
        raise TypeError
    sum_number = 1
    for x in numbers:
        if not isinstance(x, (int, float)):
            raise TypeError
        sum_number = sum_number * x
    return sum_number


# # 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


def trim(s):
    """去除字符串首尾空格"""
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


def find_min_and_max(l):
    """使用迭代查找一个list中最小和最大值，并返回一个tuple"""
    # min_number = 0 这个不科学
    # max_number = 0
    if len(l) == 0:
        return None, None
    min_number = l[0]
    max_number = l[0]
    for numbers in l:
        if numbers <= min_number:
            min_number = numbers
    for numbers in l:
        if numbers >= max_number:
            max_number = numbers
    return min_number, max_number
