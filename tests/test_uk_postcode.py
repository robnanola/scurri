import unittest
from uk_postcode import UKPostCode
from uk_postcode import InvalidFormat
from uk_postcode import DetailsNotFound

class TestUKPostCode(unittest.TestCase):
    def setUp(self):
        self.postcode_class = UKPostCode()

    def test_valid_postcode(self):
        
        self.assertTrue(self.postcode_class.is_valid('AA9A 9AA'))
        self.assertTrue(self.postcode_class.is_valid('A9A 9AA'))
        self.assertTrue(self.postcode_class.is_valid('A9 9AA'))
        self.assertTrue(self.postcode_class.is_valid('A99 9AA'))
        self.assertTrue(self.postcode_class.is_valid('AA9 9AA'))
        self.assertTrue(self.postcode_class.is_valid('AA99 9AA'))

        self.assertTrue(self.postcode_class.is_valid('AAAA 9AA'))
        self.assertTrue(self.postcode_class.is_valid('AA 99'))



    def test_invalid_postcode(self):

        self.assertFalse(self.postcode_class.is_valid('AA9A9AA'))
        self.assertFalse(self.postcode_class.is_valid('A9A9AA'))
        self.assertFalse(self.postcode_class.is_valid('A99AA'))
        self.assertFalse(self.postcode_class.is_valid('A999AA'))
        self.assertFalse(self.postcode_class.is_valid('AA99AA'))
        self.assertFalse(self.postcode_class.is_valid('AA999AA'))

        self.assertFalse(self.postcode_class.is_valid('AAAA9AA'))
        self.assertFalse(self.postcode_class.is_valid('AA99'))



    def test_get_details(self):

        details = self.postcode_class.get_post_code_details('EC1A 1BB')
        self.assertEqual(details['outcode'], 'EC1A')
        self.assertEqual(details['incode'], '1BB')

    def test_get_details_invalid_format(self):
        with self.assertRaises(InvalidFormat) as err:
            self.postcode_class.get_post_code_details('EC1A1BB')


    def test_get_details_not_found(self):
        with self.assertRaises(DetailsNotFound) as err:
            self.postcode_class.get_post_code_details('AA9 9AA')

