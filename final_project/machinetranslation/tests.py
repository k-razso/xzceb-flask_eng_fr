import unittest

from translator.py import frenchToEnglish, englishToFrench

class TestEngToFrench(unittest.TestCase)
    def testEng2Fr(self):
        # Write at least 2 tests
        self.assertEqual(englishToFrench,'man','homme')
        self.assertEqual(englishToFrench,'bread','pain')
        # Test for the translation of the world ‘Hello’ and ‘Bonjour’
        self.assertEqual(englishToFrench,'Hello','Bonjour')
        # Testing for null input
        self.assertEqual(englishToFrench,'','')
    
 class TestFrenchToEng(unittest.TestCase)   
    def testFr2Eng(self):
        # Write at least 2 tests
        self.assertEqual(frenchToEnglish,'homme','man')
        self.assertEqual(frenchToEnglish,'pain','bread')
        # Test for the translation of the world ‘Hello’ and ‘Bonjour’
        self.assertEqual(frenchToEnglish,'Bonjour','Hello')
        # Testing for null input
        self.assertEqual(frenchToEnglish,'','')

if __name__==if __name__ == "__main__":
    unittest.main()