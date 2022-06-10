#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def climbingLeaderboard(ranked, player):
    #This code took me a while!
    #Sort leaderboard scores and player scores in descending order
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)

    scoresNo = len(ranked)
    count=0
    
    ranks=[]
    #Loop through player scores
    for score in player:
        #keep increasing rank until score isn't smaller or end of list
        while count<scoresNo and score<ranked[count]:
            count+=1
        #add rank to list
        ranks.append(count+1)
        
        #return ranks mirror
    return ranks[::-1]
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
