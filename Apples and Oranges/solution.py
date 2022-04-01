#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s = houseStartRange
#  2. INTEGER t = houseEndRange
#  3. INTEGER a = appleTreePos
#  4. INTEGER b = orangeTreePos
#  5. INTEGER_ARRAY apples = appleCoordsFromA
#  6. INTEGER_ARRAY oranges = orangeCoordsFromB
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    counterA = 0;
    counterO = 0;
    for i in range(0,len(apples)):
        if(a + apples[i] >= s and a + apples[i] <= t ):
            counterA+=1
    for i in range(0,len(oranges)):
        if(b + oranges[i] >= s and b + oranges[i] <= t ):
            counterO+=1
    print(counterA)
    print(counterO)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
