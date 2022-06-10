#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Quick solution, could be better but worked first try :)
    # Write your code here
    valleysTraversed = 0
    altitude = 0
    for i in range(steps):
        if path[i] == "U":
            altitude+=1
        else:
            altitude-=1
        if(altitude == -1 and path[i+1] == "U"):
            valleysTraversed +=1
    return valleysTraversed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
