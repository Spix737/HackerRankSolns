#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    #Easy solution, probably not the best solution, but it works.
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    letters = [char for char in word]
    letters = sorted(letters)
    
    maxHeight = 0
    for i in letters:
        count = 0
        while(count<26):
            if(i==alphabet[count]):
                if(h[count] > maxHeight):
                    maxHeight = h[count]
            count+=1
    
    return maxHeight * len(word)
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
