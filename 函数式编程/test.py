#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 17:31
# @Author  : Zhang_xq
# @File    : test.py
# @Software: PyCharm

flist = []

for i in range(3):
    def func(x):
        return x * i


    flist.append(func)

for f in flist:
    print(f(2))
