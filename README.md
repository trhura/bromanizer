## About ##

Bromanizer is automatic romanization system for Burmese text, based on [BGN/PCGN 1970 Standard](http://earth-info.nga.mil/gns/html/Romanization/Romanization_Burmese.pdf)

## Usage ##

See the tests below for example usage.

```python
self.assertEqual(Romanizer.romanize(BGN_PCGN, 'ကို'), "ko")
self.assertEqual(Romanizer.romanize(BGN_PCGN, 'အက'), "aga")
self.assertEqual(Romanizer.romanize(BGN_PCGN, 'မဒမ'), "madama")
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
```

## TODO ##

* Add MLCTS and IPA transliteraions.
* Add more tests.
