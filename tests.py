#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
import unittest
import bromanizer
import helper

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_find_first_position(self):
        self.assertEqual (-1, bromanizer.find_first_position("asdf", helper.ismyanmar))
        self.assertEqual (2, bromanizer.find_first_position(u"as\u1000f", helper.ismyconsonant))

    def test_my_phonemic_iter(self):
        s = "တ|ရား|စီ|ရင်|ရေး|အာ|ဏာ|နှင့်|ဥ|ပ|ဒေ|ပြု|ရေး|အာ|ဏာ|တို့|ကို"
        ts = "".join(s.split('|'))
        tr = list(bromanizer.my_phonemic_iter(ts))
        er = list(unicode(e, 'utf-8') for e in s.split('|'))
        print ts, tr, er
        self.assertEqual (tr, er)

if __name__ == '__main__':
    unittest.main()
