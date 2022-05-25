#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

#
#Range: 1700 to 2700 - not sure what to do if outside range
# 31 y 31 30 31 30 31 31 30 31 30 31
#x > 1918: y = 28, y = 29 if x/4
#x < 1918: y = 28, y = 29 if x / 400 or x / 4 & x !/ 100 
#x = 1918: y = 14, 15 if x/4
#

def dayOfProgrammer(year):
    ###Difficult question. Simplified requirements above, then solution was simple.
    day = 13
    if year < 1918:
        if year % 4 == 0:
            day = 12
    elif year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            day = 12
    else:
        day = 26
    return (str(day) + ".09." + str(year))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
