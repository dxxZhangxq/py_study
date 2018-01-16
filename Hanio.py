#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 1:03
# @Author  : Zhang_xq
# @File    : Hanio.py
# @Software: PyCharm

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def move(n, a, b, c):
    # if not isinstance(n, int) and isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
    #     raise TypeError('fuck off')
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)
    return '移动完成'


print(move(206, 'A', 'B', 'C'))
