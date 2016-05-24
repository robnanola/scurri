#!/usr/bin/env python2.7

def print_no(num):
    """
    Print given num, but print 'Three' for multiples of three,
    'Five' for muptiples of five,
    'ThreeFive' for both multiples of three and five

    >>> print_no(25)
    >>> Five

    >>> print_no(15)
    >>> ThreeFive

    >>> print_no(12)
    >>> Three

    """

    out = ''
    if num%3 == 0:
        out += 'Three'

    if num%5 == 0:
        out += 'Five'

    if not out:
       return num

    return out

if __name__ == '__main__':
    for i in range(1,101):
        print print_no(i)
