#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-14 上午12:36
# @Author  : Zhang_xq
# @File    : err_raise.py
# @Software: PyCharm


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')