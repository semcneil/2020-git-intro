#!/usr/bin/env python3
#
# operators.py
#
# This is a file to demonstrate open source software collaboration for the
# 2020 CPTR 226 class.
#
# Author: Jared Schiavone
# Date: 2020 September 07
# Author: Kristin Sydow
# Date: 2020 September 8
# Author: Diana Celaya 
# Date: 2020 September 10
# Version: 0.1
# Course: CPTR 226
"""This is a file to demonstrate open source software collaboration for the
   2020 CPTR 226 class.
"""

# Includes
import datetime  # used for start/end times
import argparse  # This gives better commandline argument functionality
import doctest   # used for testing the code from docstring examples


# Global Variables


# Functions
def multiply_something(num1, num2):
    """this function will multiply num1 and num2

        >>> multiply_something(2, 6)
        12
        >>> multiply_something(-2, 6)
        -12
        
    """
    return(num1 * num2)


def minus_something(num1, num2):
    """This function substracts two numbers and returns the result
        
        >>> minus_something(8, 5)
        3
    """
    return(num1 - num2)

  
def not_equal(num1, num2):
    """This function determines if two numbers are equal

        >>> not_equal(2,3)
        True
        >>> not_equal(4, 4)
        False
        >>> not_equal(-3, -5)
        True
    """
    return(num1 != num2)
  

def greater_than_something(num1, num2):
    """This function checks if the first number is greater than the second.

        >>> greater_than_something(2,3)
        False
        >>> greater_than_something(-4, 4)
        False
        >>> greater_than_something(-3, -5)
        True

    """
    return(num1 > num2)
  

def is_equal(a, b):
    """This function checks if the two variables are equal to each other.

        >>> is_equal(2, 2)
        True
        >>> is_equal(2, 3)
        False
        >>> is_equal("Dog", "Dog")
        True
        >>> is_equal("Cat", "Dog")
        False
    """
    return(a == b)


def sequence(find, numbers):
    """This function checks to see if an object is in a sequence

        >>> sequence(1, [1,2,3,4])
        1
        >>> sequence("i", "Hello world")
        'Nothing'
        >>> sequence(4, (2,4,6))
        4
    """
    for n in numbers:
        if find == n:
            return(n)
    else:
        return("Nothing")

def exponet(num1, num2):
    """"This function exponentiates 2 numbers
    
        >>> exponet(2, 2)
        4
        >>> exponet(2, -2)
        0.25
    """
    return(num1**num2)

def less_than_something(num1, num2):
    """This function checks if the first number is less than the second.

        >>> less_than_something(5,9)
        True
        >>> less_than_something(2, 4)
        True
        >>> less_than_something(-8, -4)
        False
    """
    
def floor_divide(num1, num2):
    """ This function returns the integral part of the quotient 
        >>> floor_divide(5, 3)
        2
    """
    return(num1//num2)

def modulus(a, b):
    """This function finds the remainder from a division
        >>> modulus(7, 2)
        1 
    """
    return(a % b)

def modulus(a, b):
    """This function finds the remainder from a division

        >>> modulus(7, 2)
        1 
    """
    return(a % b)

# This runs if the file is run as a script vs included as a module
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--doctest', action='store_true',
                        help='Pass this flag to run doctest on the script')

    start_time = datetime.datetime.now()  # save the script start time
    args = parser.parse_args()  # parse the arguments from the commandline

    if(args.doctest):
        doctest.testmod(verbose=True)  # run the tests in verbose mode

    print("-------------------")
    print()
    multiplied = multiply_something(2, 6)
    print(f'multiply 2 x 6 = {multiplied}')

    subtracted = minus_something(8, 5)
    print(f'Subtracting 8 - 5 = {subtracted}')

    added = not_equal(4, 5)
    print(f'4 != 5 = {added}')
    
    gt = greater_than_something(4, 5)
    print(f'4 is greater than 5 = {gt}')

    equal = is_equal(5, 5)
    print(f'Is 5 equal to 5? {equal}')

    sequenced = sequence(6, [1, 2, 3, 4, 5, 6])
    print(f'{sequenced} is in the sequence')

    exponentiated = exponet(2, 2)
    print(f'2**2 = {exponentiated}')

    lt = less_than_something(1, 6)
    print(f'1 is less than 6 = {lt}')

    modulus = modulus(10, 4)
    print(f'The remainder is {modulus}')

    floor_divided = floor_divide(7,6) 
    print(f'{floor_divided} was returned by floor divide')

    end_time = datetime.datetime.now()    # save the script end time
    print(f'{__file__} took {end_time - start_time} s to complete')
