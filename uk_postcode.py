#!/usr/bin/env python2.7
import re
import requests
import json


class InvalidFormat(Exception):
    """
    Custom exception for invalid postcode format
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
        check if post_code is a valid format and return its details

        Arg:
            postcode: OX49 5NU

        Returns:
            { 
                'outcode': 'OX49',  
                'postcode': 'OX49 5NU', 
                'incode': u'5NU', 
                'area': 'OX', 
                'district':'49', 
                'sector':'5', 
                'unit':'NU'
            }

        """

        if self.is_valid(post_code):
            return self.do_parse(post_code)

        raise InvalidFormat('Invalid postcode format for {0}'.format(post_code))



    def do_parse(self, post_code):
        """
        Returns: post_code, outcode, incode, area, district, sector, unit given the post_code

        Given: PO1 3AX

        >> outcode = PO1
        >> incode = 3AX
        >> area = PO
        >> district = 1
        >> sector = 3
        >> unit = AX

        """
        regex = re.compile("([a-zA-Z]+)([0-9a-zA-Z]+)? ([0-9]+)([a-zA-Z]+)")

        result = dict(zip(('outcode', 'incode'), post_code.split()))
        result['post_code'] = post_code

        try:
            details = dict(zip(('area', 'district', 'sector', 'unit'), regex.match(post_code).groups()))
            result.update(details)
        except AttributeError:
            # special case return outcode and incode only
            pass

        return result



