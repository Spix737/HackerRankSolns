#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDistinctSubstringLengthInSessions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sessionString as parameter.
#

def maxDistinctSubstringLengthInSessions(sessionString):
    max_unique = 0

    # Split by '*' to process each session independently
    for session in sessionString.split('*'):
        seen = set()      # characters currently in the window
        left = 0          # window start index

        # Sliding window over the current session
        for right in range(len(session)):
            char = session[right]

            # If we already saw this char, shrink the window
            while char in seen:
                seen.remove(session[left])
                left += 1

            # Add current char and update max
            seen.add(char)
            max_unique = max(max_unique, right - left + 1)

    return max_unique

    # strings = sessionString.split('*')
    
    # max_unique = 0
    # for string in strings:
    #     curr = 0
    #     chars = list(string)
    #     seenChars = []
    #     for char in chars:
    #         if char not in seenChars:
    #             seenChars.append(char)
    #             curr+=1
    #             if curr > max_unique:
    #                 max_unique = curr
    #         else:
    #             i=0
    #             while chars[i] != char:
    #                 chars.remove(chars[i])
    #                 curr-=1
    
    # return max_unique
    
    

if __name__ == '__main__':
    sessionString = input()

    result = maxDistinctSubstringLengthInSessions(sessionString)

    print(result)
