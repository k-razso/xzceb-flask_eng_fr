import unittest
from translator import french_to_english, english_to_french

class TestEngToFrench(unittest.TestCase):
    def testEng2Fr(self):
        # Write at least 2 tests
        self.assertEqual(english_to_french('man'),'homme')
        self.assertEqual(english_to_french('bread'),'pain')
        # Test for the translation of the world ‘Hello’ and ‘Bonjour’
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        # Testing for null input
        #self.assertEqual(english_to_french,'','')
    
class TestFrenchToEng(unittest.TestCase):
    def testFr2Eng(self):
        # Write at least 2 tests
        self.assertEqual(french_to_english('homme'),'man')
        self.assertEqual(french_to_english('pain'),'bread')
        # Test for the translation of the world ‘Hello’ and ‘Bonjour’
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        # Testing for null input
        #self.assertEqual(french_to_english,'','')

if __name__ == "__main__":
    unittest.main()
