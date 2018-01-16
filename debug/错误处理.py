#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-14 上午12:08
# @Author  : Zhang_xq
# @File    : 错误处理.py
# @Software: PyCharm

from functools import reduce

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except', e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / 1.7
    print('result:', r)
except ZeroDivisionError as e:
    print('except', e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
except ValueError as e:
    print('ValueError', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar(7)
    except Exception as e:
        print('ERROR:', e)
        # else:
        # print(bar(7))
    finally:
        print('END')


print(main())


# 练习
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
# from functools import reduce

# def str2num(s):
    # return int(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()
def str2num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
