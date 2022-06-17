#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n - prisoner number
#  2. INTEGER m - candy number
#  3. INTEGER s - chairStart
#

def saveThePrisoner(n, m, s):
    # Great solution inspired by google.
    #(chairStart + candyNumber - 1) % prisonerNumber
    endPos = (s+m-1)%n
    if endPos!=0:
        return endPos
    else:
        return n
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
