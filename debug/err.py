#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-14 上午12:23
# @Author  : Zhang_xq
# @File    : err.py
# @Software: PyCharm
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')
