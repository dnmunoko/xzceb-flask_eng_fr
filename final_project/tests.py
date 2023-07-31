from translator import englishtofrench,frenchtoenglish
import unittest

class testenfr(unittest.TestCase):
    def test_eng_fr(self):
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertEqual(englishtofrench('Come'),'Venir')
        self.assertEqual(englishtofrench(''),'Empty')
        self.assertNotEqual(englishtofrench('Good'),'Bien')

class testfren(unittest.TestCase):
    def test_fr_eng(self):
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertEqual(frenchtoenglish('Venir'),'Come')
        self.assertEqual(frenchtoenglish(''),'Empty')
        self.assertNotEqual(frenchtoenglish('Bien'),'Good')

unittest.main()