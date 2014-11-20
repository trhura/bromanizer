#! /usr/bin/env python3
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

    def test_myanmar_phonemic_iter(self):
        def test_myanmar_phonemic_iter_(string, ts=None):
            if not ts: ts = "".join(string.split('|'))
            tr = list(bromanizer.myanmar_phonemic_iter(ts))
            er = list(e for e in string.split('|'))
            self.assertEqual (tr, er)

        test_myanmar_phonemic_iter_("တ|ရား|စီ|ရင်|ရေး|အာ|ဏာ|နှင့်|ဥ|ပ|ဒေ|ပြု|ရေး|အာ|ဏာ|တို့|ကို")
        test_myanmar_phonemic_iter_("မည်|သူ|မ|ဆို| |ကြည့်|ရှု|ပြင်|ဆင်|နိုင်|သော| |အ|ခ|မဲ့|လွတ်|လပ်|စွယ်|စုံ|ကျမ်း| |ဖြစ်|ပါ|သည်|။")
        test_myanmar_phonemic_iter_("နာ|နို|တက်|က|နော်|လော်|ဂျီ" , ts="နာနိုတက္ကနော်လော်ဂျီ")
        test_myanmar_phonemic_iter_("အို|ရှန်း|နီး|ယား")

    def test_bgp_pcgn_romanizer(self):
        from bromanizer import Romanizer, BGN_PCGN
        self.assertEqual(Romanizer.romanize(BGN_PCGN, 'ကို'), "ko")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, 'အက'), "aga")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, 'မဒမ'), "madama")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, 'သာငယ္'), 'thangè')
        self.assertEqual(Romanizer.romanize(BGN_PCGN, 'ပြစင်'), 'pyazin')
        self.assertEqual(Romanizer.romanize(BGN_PCGN, 'အကာ'), 'aga')
        self.assertEqual(Romanizer.romanize(BGN_PCGN, 'အိုဘဲ့'), 'obè')
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "အပ်"), "at")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "မအူ"), "ma-u")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "သီးပင်အိုင်"),'thibin-aing')
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ဩဘာ"), "awba")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ဧဏီ"), "eni")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ကြောင်ဥကျဉ်"), "kyaung-ugyin")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "သဒ္ဒါ"), "thadda")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "အန္တိမဘဝ"), "andimabawa")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ဥက္ကဌ"), "ukkada")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ရွှေငန်း"),"shwengan")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ညီညာ"), "nyinya")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "အင်းကွတ်"),"in-gut")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ကွန်ရက်"),"kun-yet")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "တိုင်အောင်"), "taing-aung")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ဟက်ဟက်ပက်ပက်ရယ်"),"het-hetpetpetyè")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ဝသီ"), "wathi")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ဘေးမဲ့"), "bemè")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "သင်္ဘော"),"thinbaw")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "ဘင်္ဂလားအော်"), "bin-gala-aw")
        self.assertEqual(Romanizer.romanize(BGN_PCGN, "စင်္ကာပူ"),"sin-gabu")

if __name__ == '__main__':
    unittest.main()
