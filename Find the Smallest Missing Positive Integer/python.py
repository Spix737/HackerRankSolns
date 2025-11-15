#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

# Since the array has elements, the smallest missing positive integer must be between 1 and N+1
# This means we can "sort" the array using In-Place Hashing, using the input array itself as a temporary hash map.
# We swap items into their correct "index" position, skipping over any items larger than len/N as we KNOW they won't be the smallest and can skip
#  them, same skip with negatives as it MUST be positive!

# After placing all valid numbers, we scan the array from i=0 to N-1. The moment we find a mismatch where (value != index + 1) the value at index is not equal to the expected value (i+1) we know that is the smallest missing positive integer.


def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)

    # 1. place values in "index = value - 1" positions
    i = 0
    while i < n:
        v = orderNumbers[i]
        # Check: valid range AND not already in correct position
        if 1 <= v <= n and orderNumbers[v - 1] != v:
            orderNumbers[i], orderNumbers[v - 1] = orderNumbers[v - 1], orderNumbers[i]
        else:
            i += 1

    # 2. scan for the first index where value != index + 1
    for i in range(n):
        if orderNumbers[i] != i + 1:
            return i + 1

    # If all filled correctly
    return n + 1

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
