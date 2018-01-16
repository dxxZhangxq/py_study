#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 15:28
# @Author  : Zhang_xq
# @File    : higher_order_function.py
# @Software: PyCharm

print(abs(-10))
print(abs)

x = abs(-10)
print(x)
f = abs
print(f(-202))

# abs = [203]
# print(abs(-232))


def add(x_1, y, z):
    """test"""
    return z(x_1) + z(y)


z = abs
print(add(-4, -5, z))
