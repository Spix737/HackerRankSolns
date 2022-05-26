#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    #Simple solution, uses array as dictionary which is slow in cases with few numbers.
    #Uses int division to remove decimal.
    numDict = []
    for i in range(0,101):
        numDict.append(0)
    for i in range(len(ar)):
        numDict[ar[i]] = numDict[ar[i]] + 1
    pairs = 0
    for i in range(len(numDict)):
        pairs += int(numDict[i] / 2)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
