#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    #I had initially written the code in the comments written below.
    #However, upon conducting some research I encountered a significantly more elegant solution.
    #I decided to incorporate that one to encourage me to learn better solutions.
    maxArrayA = max(a)
    minArrayB = min(b)
    count = 0
    """
    for num in range(maxArrayA, minArrayB + 1):
        condition1 = True
        for numA in a:
            if num % numA != 0:
                condition1 = False
                break
        condition2 = True
        for numB in b:
            if numB % num != 0:
                condition2 = False
                break
        count += condition1 * condition2
    """
    for num in range(maxArrayA, minArrayB + 1):
        left = all([num % numA == 0 for numA in a])
        right = all([numB % num == 0 for numB in b])
        count += left * right
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

