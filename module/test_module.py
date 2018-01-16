#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-10 下午3:32
# @Author  : Zhang_xq
# @File    : test_module.py
# @Software: PyCharm Community Edition
import sys

"a test module"
__author__ = 'Zhangxq'


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello, world')
    elif len(args) == 2:
        print('hello, %s' % args[1])
    else:
        print('too many arguments!')


if __name__ == '__main__':
    test()
