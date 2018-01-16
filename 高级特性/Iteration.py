#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 18:28
# @Author  : Zhang_xq
# @File    : Iteration.py
# @Software: PyCharm

from collections import Iterable

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key)

for key in D.values():
    print(key)

for key, values in D.items():
    print(key, values)

print(isinstance('abs', Iterable))
print(isinstance([1, 3, 4], Iterable))
print(isinstance(2, Iterable))

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)


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


# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
