#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    #-------------------
    #THIS SOLUTION FELT JANK 
    #If they move at the same pace (need to account for start positions but hackerrank assumes the start position is different or else it'd be redundant i guess so no need to code it but important to remember.)
    #If either velocity is zero
    #! If the remainder of distance over velocity is not zero
    #If they move in opposite directions
    if v1==v2 or v1==0 or v2==0 or ((x1 - x2) % (v2-v1)) != 0 or ((x1 - x2) / (v2-v1)) <= 0:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
