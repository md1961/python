import unittest
from subsequence_finder import SubseqenceFinder

class SubseqenceFinderTest(unittest.TestCase):

    def test_is_subsequence(self):
        sf = SubseqenceFinder('abppplee')

        self.assertTrue(sf.is_subsequence('abppplee'))
        self.assertTrue(sf.is_subsequence('abpplee'))
        self.assertTrue(sf.is_subsequence('a'))
        self.assertTrue(sf.is_subsequence('e'))

        self.assertFalse(sf.is_subsequence('abppleee'))
        self.assertFalse(sf.is_subsequence('abbpplee'))

        self.assertTrue(sf.is_subsequence('able'))
        self.assertTrue(sf.is_subsequence('ale'))
        self.assertTrue(sf.is_subsequence('apple'))

        self.assertFalse(sf.is_subsequence('bale'))
        self.assertFalse(sf.is_subsequence('kangaroo'))

    def test_longest_subsequence(self):
        sf = SubseqenceFinder('abppplee')

        self.assertEqual(sf.longest_subsequence([]), '')

        array = ['able', 'ale', 'apple', 'bale', 'kangaroo']
        self.assertEqual(sf.longest_subsequence(array), 'apple')

        array = ['able', 'ale', 'apple', 'bale', 'kangaroo', 'abppplee']
        self.assertEqual(sf.longest_subsequence(array), 'abppplee')
