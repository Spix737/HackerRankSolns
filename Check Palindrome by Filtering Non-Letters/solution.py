#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # Convert to lowercase
    code = code.lower()

    # Keep only alphabetic characters
    cleaned = re.sub('[^a-z]', '', code)
    # without regex
    # cleaned = ''.join(ch for ch in code if ch.isalpha())

    # Check palindrome
    return cleaned == cleaned[::-1]

    """
    General slicing form
    string[start : stop : step]
    start = where to begin (default is beginning)
    stop = where to end (default is end)
    step = how much to move each time
    • 1 means forward
    • -1 means backward

    Here we:
    - start from the end (because step = -1)
    - go backwards one character at a time
    - stop once the beginning is reached
    """


if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
