#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    
    if len(a)==0:
        return 0
    #Not concerned with specific sort - pythons problem
    a.sort()
    subArrayCount = 0
    counts = []
    start = a[0]
    #If the difference between any two elements is less than
    #or equal to 1, increase subarray length count.
    #Else record subarray length, start a new subarray len 1,
    #and set start to the index of next subarray start
    for i in a:
        if abs(i-start)<=1:
            subArrayCount+=1
        else:
            counts.append(subArrayCount)
            subArrayCount = 1
            start = i
    counts.append(subArrayCount)    
    return max(counts)

    # countNums = Counter(a)
    # maxnum=0
    # for i in range(1, 100):
    #      maxnum = max(maxnum, countNums[i]+countNums[i+1])                      
    # return maxnum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
