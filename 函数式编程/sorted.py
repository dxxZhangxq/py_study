#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 0:49
# @Author  : Zhang_xq
# @File    : sorted.py
# @Software: PyCharm

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 练习
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    """按照姓名排序"""
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)

# 再按成绩从高到低排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    """按照成绩排序"""
    return t[1]*-1


L2 = sorted(L, key=by_score)
print(L2)
