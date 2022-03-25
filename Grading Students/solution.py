#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    gradess = []
    for i in range(0, len(grades)):
        if grades[i] < 38 or grades[i] % 5 == 0:
            gradess.append(grades[i])
            continue
        elif (grades[i] % 5 )>2:
            gradess.append(grades[i] + 5 - (grades[i] % 5))
            continue
        gradess.append(grades[i])
    return gradess

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
