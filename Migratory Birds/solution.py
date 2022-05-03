#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    #2nd attempt. Much quicker. Uses dictionary. Smart.

    #Fetch initial count of each bird.
    #As we are given a constraint of 5 birds, we can use a dictionary to store the count.
    bird_count = [0]*6
    for i in arr:
        bird_count[i] += 1
    #Find the max count
    max_count = max(bird_count)
    #Find the index of the max count
    max_index = bird_count.index(max_count)
    return max_index
    
    """
    #Initial solve - works, but extremely inefficient as it runs n*n times
    oldCount = 0
    oldBird = 0
    for i in range(len(arr)):
        count = 0
        bird = 0
        if arr[i] != bird:
            bird = arr[i]
        else:
            continue
        for j in range(len(arr)):
            if arr[j] == bird:
                count+=1
        if i != 0:
            if count > oldCount:
                oldCount = count
                oldBird = bird
            if count == oldCount:
                oldBird = min(bird, oldBird)
    return oldBird
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
