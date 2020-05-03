'''
Created on Mar 26, 2018

@author: ksm
'''
import unittest
import CleverHangman as ch

class TestCreateTemplate(unittest.TestCase):


    def outline(self, currTemplate, letter, word, expect):
        result = ch.createTemplate(currTemplate, word, letter)
        msg = 'Called createTemplate({}, {}, {}), expected "{}" got "{}"'.format(
            repr(currTemplate), repr(letter), repr(word), expect, result)
        self.assertEqual(result, expect, msg)


    def testBlankTemplateLetterNotInWord(self):
        self.outline('___', 'a', 'for', '___')


    def testBlankTemplateLetterIsInWord(self):
        self.outline('___', 'a', 'far', '_a_')


    def testNonBlankTemplateLetterNotInWord(self):
        self.outline('t___', 'a', 'trim', 't___')


    def testNonBlankTemplateLetterIsInWord(self):
        self.outline('w_l_', 't', 'wilt', 'w_lt')


    def testAlmostDoneTemplateLetterNotInWord(self):
        self.outline('w_ll', 'a', 'will', 'w_ll')


    def testAlmostDoneTemplateLetterIsInWord(self):
        self.outline('w_ll', 'i', 'will', 'will')


class TestGetNewWordList(unittest.TestCase):


    def outline(self, currTemplate, letter, words, expectTemplate, expectSet):
        result = ch.getNewWordList(currTemplate, letter, words)
        msg = 'Called getNewWordList({}, {}, {}), expected template: "{}" got: "{}"'.format(
            repr(currTemplate), repr(letter), repr(words), expectTemplate,
            result[0])
        self.assertEqual(result[0], expectTemplate, msg)

        msg = 'Called getNewWordList({}, {}, {}), expected list: {} got: {}'.format(
            repr(currTemplate), repr(letter), repr(words), list(expectSet),
            result[1])
        self.assertEqual(set(result[1]), expectSet, msg)

    
    def testShouldKeepCurrTemplate(self):
        words = ['has', 'had', 'gin', 'icy', 'few']
        self.outline('___', 'a', words, '___', {'gin', 'icy', 'few'})


    def testShouldNotKeepCurrTemplate(self):
        words = ['has', 'had', 'gin']
        self.outline('___', 'a', words, '_a_', {'has', 'had'})


    def testNoChoicesLeft(self):
        words = ['trim', 'trio']
        self.outline('t___', 'r', words, 'tr__', set(words))


    def testPreventGuess(self): 
        words = ['trim', 'trio']
        self.outline('tri_', 'm', words, 'tri_', {'trio'})


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()