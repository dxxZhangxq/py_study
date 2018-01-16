#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-15 下午6:02
# @Author  : Zhang_xq
# @File    : 文档测试.py
# @Software: PyCharm


# def abs_1(n):
#     """
#     Function to get absolute value of number.
#
#     Example:
#
#     >>>abs_1(1)
#     1
#     >>>abs_1(-1)
#     1
#     >>>abs_1(0)
#     0
#     """
#     return n if n >= 0 else -n
from module.test_module import test


class DictH(dict):
    """
    Simple Dict but also support access as x.y style.
    
    >>>d1 = DictH()
    >>>d1['x'] = 100
    >>>d1.x
    100
    >>>d1.y = 200
    >>>d1['y']
    200
     >>> d2 = DictH(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    """

    def __init__(self, **kwargs):
        super(DictH, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict_1' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
