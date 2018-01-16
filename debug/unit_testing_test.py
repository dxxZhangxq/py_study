#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-1-15 上午1:20
# @Author  : Zhang_xq
# @File    : unit_testing_test.py
# @Software: PyCharm
import unittest
from debug.unit_testing import DictH


class TestDict(unittest.TestCase):
    def test_init(self):
        d = DictH(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = DictH()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = DictH()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_key_error(self):
        d = DictH()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attr_error(self):
        d = DictH()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print('setUP...')

    def tearDown(self):
        print('tearDOWN...')

if __name__ == '__main__':
    unittest.main()
