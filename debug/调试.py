#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-15 上午12:08
# @Author  : Zhang_xq
# @File    : 调试.py
# @Software: PyCharm
import logging
import pdb


def foo(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n


def main():
    foo('0')


# main()

s_1 = '0'
n = int(s_1)
pdb.set_trace()
print(10 / n)