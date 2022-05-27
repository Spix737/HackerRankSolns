#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    #Simple, even added error handling :) 
    AC = abs(x - z)
    BC = abs(y - z)
    if(AC==BC):
        return("Mouse C")
    elif(AC>BC):
        return("Cat B")
    elif(AC<BC):
        return("Cat A")
    else:
        return("Error")
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
