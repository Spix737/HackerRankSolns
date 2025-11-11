#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findZeroSumTripletsInWindow' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY readings
#  2. INTEGER windowSize
#
def findZeroSumTripletsInWindow(readings: list[int], windowSize: int) -> set[tuple[int, int, int]]:
    n = len(readings)
    found = set()
    
    # Loop over all possible window starts
    for start in range(n):
        # get the window by iterating a window size over the array..!
        window = readings[start:start + windowSize]
        # don't account for end cases where the window size is < windowSize param
        if len(window) < 3:
            continue
        
        # perform 3-sum within this window
        # a + b + c = 0
        window.sort()       # O(n log n)
        
        # -2 accounts for len/index and for 'a' being taken out (what we compare against) 
        for i in range(len(window) - 2):        # O(n)
            # The continue line skips duplicates so that we don’t repeat the same a value for multiple triplets.
            if i > 0 and window[i] == window[i - 1]:
                continue
                    
            # l (left pointer) starts just after i.
            # r (right pointer) starts at the end of the array.
            # These will scan inward looking for b and c.
            l, r = i + 1, len(window) - 1
            
            # Once the pointers meet, all pairs with the fixed i have been examined.
            # Then the outer loop increments i, fixing a new first element, and repeats the process. 
            while l < r:        # O(n), pointers move towards one another and collab to O(n) vs O(n^2) in a naive soln without coordinated pointers
                s = window[i] + window[l] + window[r]
                if s == 0:
                    # We found a valid triplet:
                    found.add((window[i], window[l], window[r]))
                    # move both pointers inward (l += 1, r -= 1),
                    l += 1
                    r -= 1
                    # skip duplicates, ensuring unique triplets only. checking and skipping is intrinsically better than writing all and then pruning duplicates, or using a set to do so during.
                    while l < r and window[l] == window[l - 1]:
                        l += 1
                    while l < r and window[r] == window[r + 1]:
                        r -= 1
                        
                # The sum is too small.
                # Since the array is sorted, we can increase the sum by moving l rightwards:
                elif s < 0:
                    l += 1
                    
                # The sum is too large.
                # Decrease it by moving r leftwards
                else:
                    r -= 1
    
    return [list(triplet) for triplet in found]

if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = int(input().strip())
        readings.append(readings_item)

    windowSize = int(input().strip())

    result = findZeroSumTripletsInWindow(readings, windowSize)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
