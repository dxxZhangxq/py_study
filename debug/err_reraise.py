#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-14 上午12:38
# @Author  : Zhang_xq
# @File    : err_reraise.py
# @Software: PyCharm


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value1: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input Er2222ror!')