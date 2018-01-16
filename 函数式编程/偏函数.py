#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-10 下午3:12
# @Author  : Zhang_xq
# @File    : 偏函数.py
# @Software: PyCharm Community Edition
import functools

print(int('10110010', base=2))


def int2(x, base=2):
    return int(x, base)


print(int2('10110010'))

int2_1 = functools.partial(int, base=2)
print(int2_1('10110010'))

max_1 = functools.partial(max, 10)
print(max_1(1, 3, 4, 5, 6))
