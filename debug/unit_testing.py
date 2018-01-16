#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-15 上午1:12
# @Author  : Zhang_xq
# @File    : unit_testing.py
# @Software: PyCharm


class DictH(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict_1' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
