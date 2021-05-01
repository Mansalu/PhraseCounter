import unittest
from PhraseCounter import *

class TestPhraseCounter(unittest.TestCase):

    def test_GetNgramsSimple(self):
        inputTokens = [1, 2, 3, 4, 5]
        expectedTrigrams = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        expectedBigrams = [[1,2], [2,3], [3,4], [4,5]]
        self.assertEqual(GetNgrams(inputTokens, 3), expectedTrigrams)
        self.assertEqual(GetNgrams(inputTokens, 2), expectedBigrams)

    def test_GetPhrasesSimple(self):
        inputString = 'the quick brown fox jumps over the lazy dog'
        expectedPhrases = ['the quick brown', 'quick brown fox', 'brown fox jumps',
                           'fox jumps over', 'jumps over the', 'over the lazy', 'the lazy dog']
        self.assertEqual(GetPhrases(inputString, 3), expectedPhrases)

    def test_GetPhrasesCleaningPunctuation(self):
        inputString = 'tHE qUiCK! bro@wn\' FOX!? ju(m$%p*eD.'
        expectedPhrases = ['the quick brown', 'quick brown fox', 'brown fox jumped']
        self.assertEqual(GetPhrases(CleanInputText(inputString), 3), expectedPhrases)

    def test_GetPhrasesCleaningSplitWords(self):
        inputString = 'hell-\no world! This is a fi-\nle with words tha-\nt are split acc-\nross lines'
        expectedPhrases = ['hello world this is', 'world this is a', 'this is a file', 
                           'is a file with', 'a file with words', 'file with words that', 
                           'with words that are', 'words that are split', 'that are split accross', 
                           'are split accross lines']
        self.assertEqual(GetPhrases(CleanInputText(inputString), 4), expectedPhrases)

    def test_GetPhrasesCleaningContractions(self):
        inputString = 'don\'t shouldn\'t can\'t you\'re i\'m aren\'t'
        expectedPhrases = ['dont shouldnt cant', 'shouldnt cant youre', 'cant youre im', 'youre im arent']
        self.assertEqual(GetPhrases(CleanInputText(inputString), 3), expectedPhrases)

    def test_GetTopPhrasesSmallComplexFile(self):
        inputString = ""
        try:
            textFile = open("testFiles/small_complex.txt", 'r', encoding='utf-8')
            inputString = CleanInputText(textFile.read())
        except OSError as Error:
            print("File could not be opened:", Error)
        finally:
            textFile.close()
        expectedPhrases = [("this file is", 5), ("lots of edge", 3), ("file is supposed", 2)]
        self.assertEqual(GetTopPhrases(inputString, 3, 3), expectedPhrases)

    # End to end regression tests (large files)
    def test_GetTopPhrasesMobyDick(self):
        inputString = ""
        try:
            textFile = open("testFiles/moby_dick.txt", 'r', encoding='utf-8')
            inputString = CleanInputText(textFile.read())
        except OSError as Error:
            print("File could not be opened:", Error)
        finally:
            textFile.close()
        expectedPhrases = [('the sperm whale', 84), ('the white whale', 71), ('of the whale', 70)]
        self.assertEqual(GetTopPhrases(inputString, 3, 3), expectedPhrases)
    
    def test_GetTopPhrasesWizardOfOz(self):
        inputString = ""
        try:
            textFile = open("testFiles/wizardOfOz.txt", 'r', encoding='utf-8')
            inputString = CleanInputText(textFile.read())
        except OSError as Error:
            print("File could not be opened:", Error)
        finally:
            textFile.close()
        exceptedPhrases = [('the tin woodman', 112), ('the wicked witch', 57), 
                           ('the emerald city', 54), ('said the scarecrow', 36), ('witch of the', 30)]
        self.assertEqual(GetTopPhrases(inputString, 3, 5), exceptedPhrases)

    def test_GetTopPhrasesUnicodeFile(self):
        inputString = ""
        try:
            textFile = open("testFiles/les_mis.txt", 'r', encoding='utf-8')
            inputString = CleanInputText(textFile.read())
        except OSError as Error:
            print("File could not be opened:", Error)
        finally:
            textFile.close()
        expectedPhrases = [('il y a', 123), ('monsieur le maire', 100), ('il y avait', 91), 
                           ('tout à coup', 44), ('je ne sais', 43)]
        self.assertEqual(GetTopPhrases(inputString, 3, 5), expectedPhrases)

    def test_GetTopPhrasesNotEnoughWords(self):
        inputString = "hello world"
        expectedPhrases = []
        self.assertEqual(GetTopPhrases(inputString, 3, 100), expectedPhrases)

if __name__ == '__main__':
    unittest.main()