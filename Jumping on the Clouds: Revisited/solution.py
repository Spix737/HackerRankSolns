#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    currentCloud = k % n
    e = 100 - 1 - c[currentCloud]*2
    while currentCloud != 0:
        currentCloud = (currentCloud+ k) % n
        e -= 1 + c[currentCloud]*2
        
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
