import unittest
import sys
import io
from getting_to_philosophy import find_philosophy, get_next_url, remove_paren, MAX_HOPS

class TestPhilosophy(unittest.TestCase):

    def test_remove_paren(self):
        test_str = '(hello[123]world[testing[123]])hello[ ](abc (def)) world( )'
        self.assertEqual('hello world', remove_paren(test_str))
    
    def test_remove_paren_no_change(self):
        self.assertEqual('hello world', remove_paren('hello world'), 'since there are no parentheses, the string should not change')

    def test_get_next_url_valid(self):
        result = get_next_url('https://en.wikipedia.org/wiki/Epistemology')
        self.assertIsNone(result[1])
        self.assertEqual(result[0], 'https://en.wikipedia.org/wiki/Outline_of_philosophy', 'next wikipedia page should be Outline_of_philosophy')
    
    def test_get_next_url_invalid(self):
        result = get_next_url('abc')
        self.assertIsNone(result[0])
        self.assertEqual(result[1], 'Invalid URL \'abc\': No schema supplied. Perhaps you meant http://abc?')
    
    def test_find_philosophy_valid(self):
        self.assertEqual(2, find_philosophy('https://en.wikipedia.org/wiki/Epistemology'), 'hops should be 2')
    
    def test_find_philosophy_invalid(self):
        self.assertRaises(Exception, find_philosophy, 'abcdefg')

    def test_find_philosophy_loop(self):
        self.assertEqual(MAX_HOPS, find_philosophy('https://en.wikipedia.org/wiki/Coffee_preparation'), 'hops should be ' + str(MAX_HOPS))
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPhilosophy))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()

    # suppress stdout
    suppress_text = io.StringIO()
    sys.stdout = suppress_text 

    runner.run(test_suite)

    # release stdout
    sys.stdout = sys.__stdout__
