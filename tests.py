#!/usr/bin/env python
# encoding=utf-8


import unittest

from cel import cel


class TestCELConversion(unittest.TestCase):

    def test_units(self):
        self.assertEqual(cel(0), u"zéro")
        self.assertEqual(cel(1), u"un")
        self.assertEqual(cel(2), u"deux")
        self.assertEqual(cel(3), u"trois")
        self.assertEqual(cel(4), u"quatre")
        self.assertEqual(cel(5), u"cinq")
        self.assertEqual(cel(6), u"six")
        self.assertEqual(cel(10), u"dix")
        self.assertEqual(cel(11), u"onze")
        self.assertEqual(cel(12), u"douze")
        self.assertEqual(cel(16), u"seize")

    def test_tens(self):
        self.assertEqual(cel(20), u"vingt")
        self.assertEqual(cel(30), u"trente")
        self.assertEqual(cel(40), u"quarante")
        self.assertEqual(cel(50), u"cinquante")
        self.assertEqual(cel(60), u"soixante")
        self.assertEqual(cel(70), u"soixante-dix")
        self.assertEqual(cel(80), u"quatre-vingt")
        self.assertEqual(cel(90), u"quatre-vingt-dix")

    def test_andone(self):
        self.assertEqual(cel(21), u"vingt-et-un")
        self.assertEqual(cel(31), u"trente-et-un")
        self.assertEqual(cel(41), u"quarante-et-un")
        self.assertEqual(cel(51), u"cinquante-et-un")
        self.assertEqual(cel(61), u"soixante-et-un")
        self.assertEqual(cel(121), u"cent vingt-et-un")
        self.assertEqual(cel(461), u"quatre cent soixante-et-un")

    def test_andeleven(self):
        self.assertEqual(cel(71), u"soixante-et-onze")
        self.assertEqual(cel(91), u"quatre-vingt onze")

    def test_nounits(self):
        self.assertEqual(cel(200), u"deux cent")
        self.assertEqual(cel(2000), u"deux mille")

    def test_bignums(self):
        self.assertEqual(cel(32571), u"trente deux mille " \
                                      "cinq cent soixante-et-onze")
        self.assertEqual(cel(203), u"deux cent trois")
        self.assertEqual(cel(2000000), u"deux million")
        self.assertEqual(cel(73591228), u"soixante treize million cinq " \
                                         "cent quatre-vingt onze mille deux " \
                                         "cent vingt huit")


if __name__ == '__main__':
    unittest.main()
