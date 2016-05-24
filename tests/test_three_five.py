import unittest
from threefive import print_no

class TestThreeFive(unittest.TestCase):
    def test_print_no(self):
        self.assertEqual(print_no(1), 1)
        self.assertEqual(print_no(7), 7)


    def test_print_multples_of_three(self):
        self.assertEqual(print_no(3), 'Three')
        self.assertEqual(print_no(12), 'Three')
        self.assertEqual(print_no(18), 'Three')


    def test_print_multiples_of_five(self):
        self.assertEqual(print_no(5), 'Five')
        self.assertEqual(print_no(25), 'Five')
        self.assertEqual(print_no(1010), 'Five')


    def test_print_multiples_of_three_and_five(self):
        self.assertEqual(print_no(15), 'ThreeFive')
        self.assertEqual(print_no(60), 'ThreeFive')
        self.assertEqual(print_no(90), 'ThreeFive')


    def test_invalid_value(self):
        with self.assertRaises(TypeError) as err:
            print_no('Not A Number')

