#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-10 上午12:37
# @Author  : Zhang_xq
# @File    : 装饰器.py
# @Software: PyCharm Community Edition

import functools

import time


def now():
    """打印时间"""
    return '2017-1-10'


f = now
print(f())
print(now.__name__)
print(f.__name__)


def log(func):
    """log"""

    def wrapper(*args, **kw):
        """wrapper"""
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    return '2017'


print(now())


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('hahaha')
def now():
    return '2071'


print(now())
print(now.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, *kw)

    return wrapper


def log_2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log
def now():
    return '2071'


print(now())
print(now.__name__)


@log_2('fuck')
def now():
    return 'w23'


print(now())
print(now.__name__)


# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    # @functools.wraps(fn)
    def decorator(*args, **kw):
        t = time.time()
        f = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, 1000 * (time.time() - t)))
        return f

    return decorator

    # 测试


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
