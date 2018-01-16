#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 0:56
# @Author  : Zhang_xq
# @File    : List Comprehensions.py
# @Software: PyCharm

names_up = []
for x in range(1, 11):
    names_up.append(x * x)
print(names_up)
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in '甲乙丙'])

# print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for value, key in d.items():
    print(value, ':', key)

print([v + ' : ' + k for v, k in d.items()])
names_up = ['IBM', 'PENTAX', 'CANON', 'NIKON']
print([names.lower() for names in names_up])
names_low = [n.lower() for n in names_up]
print([names.upper() for names in names_low])

# 修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'apple', None]
L2 = [words.lower() for words in L1 if isinstance(words, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
