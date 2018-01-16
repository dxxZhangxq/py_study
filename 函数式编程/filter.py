#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 0:17
# @Author  : Zhang_xq
# @File    : filter.py
# @Software: PyCharm


def is_odd(n):
    """返回偶数"""
    return n % 2 == 0


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 123])))


def not_empty(s):
    """把一个序列中的空字符串删掉"""
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B b ', None, 'C', '  '])))


def _odd_iter():
    """构造一个从3开始的奇数序列"""
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    """这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列"""
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1024:
        print(n)
    else:
        break


# 练习
# 回数是指从左向右读和从右向左读都一样的数，例如12321，909.请利用filter()筛选出回数：
def is_palindrome(n):
    """筛选回数"""
    return str(n) == str(n)[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
l200 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]
if list(filter(is_palindrome, range(1, 200))) == l200:
    print('测试成功!')
else:
    print('测试失败!')
