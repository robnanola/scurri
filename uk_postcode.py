#!/usr/bin/env python2.7
import re
import requests
import json


class InvalidFormat(Exception):
    """
    Custom exception for invalid postcode format
    """
    pass

class DetailsNotFound(Exception):
    """
    Custom exception for null details return from POSTCODE_IO_URL
    """
    pass


class UKPostCode(object):
    """
        Simple class that Validates a given post code. 
    """

    def __init__(self):
        self.REGEXs = [
            r"\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b", 
            r"\b[A-Z]{4}? [0-9][ABD-HJLNP-UW-Z]{2}\b", 
            r"\b[A-Z]{2}? [0-9]{2}\b" 
        ]

        self.POSTCODE_IO_URL = "http://api.postcodes.io/postcodes/"


    def is_valid(self, post_code):
        """
        Validates given postcode if it matches UK postcodes format. 
        Returns True if valid else False

        valid formats, where A == letter, 9 == number:
            AA9A 9AA
            A9A 9AA
            A9 9AA
            A99 9AA
            AA9 9AA
            AA99 9AA

        Special Cases post codes:
            AAAA 9AA
            AA 99
        """

        for REGEX in self.REGEXs:
            if re.match(REGEX, post_code):
                return True

        return False


    def get_post_code_details(self, post_code):
        """
        Lazy method to get post_code details via http://postcodes.io/ 

        Sample request:
            http://postcodes.io/OX49 5NU

        Sample response:
            { u'eastings': 464447, u'outcode': u'OX49', u'admin_county': u'Oxfordshire', 
            u'postcode': u'OX49 5NU', u'incode': u'5NU'}

        """

        if self.is_valid(post_code):
            response = requests.get(self.POSTCODE_IO_URL + post_code).json()

            if response['status'] == 200:
                return response['result']

            raise DetailsNotFound('No details found for {0}'.format(post_code))

        raise InvalidFormat('Invalid postcode format for {0}'.format(post_code))
