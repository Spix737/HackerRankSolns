#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Efficient solution, uses two counters in one while loop, whichever one triggers the while-and exit is the lesser pageTurnNo.
    # Write your code here
    currentPageUp = 1
    currentPageDown = n
    if(n%2!=0):
        currentPageDown -=1
        
    pageTurns = 0
    while ((currentPageUp < p) and (currentPageDown > p)):
        currentPageUp +=2
        currentPageDown -=2
        pageTurns +=1
    return pageTurns
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
