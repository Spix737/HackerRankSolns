#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findLongestArithmeticProgression' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#



def findLongestArithmeticProgression(arr: list[int], k: int) -> int:
    """
    Finds the length of the longest arithmetic subsequence with a given difference k.
    
    Time Complexity: O(N) where N is the number of unique elements.
    Space Complexity: O(N) for the DP map.
    """
    if not arr:
        return 0
            
    # 1. Remove duplicates and sort the unique elements.
    unique_sorted_arr = sorted(list(set(arr)))
    
    # 2. Dynamic Programming (DP) using a Hash Map (Dictionary)
    # Key: Element value (x)
    # Value: Length of the longest arithmetic subsequence ending at x with difference k
    dp = {}
    max_length = 0
    
    # Iterate through each unique element x
    for x in unique_sorted_arr:
        
        # Calculate the required predecessor value
        predecessor = x - k
        
        # 3. Apply the Recurrence Relation (DP step)
        # Check if the predecessor (x-k) has already established a sequence.
        
        # Python Trick: Use .get() for concise lookup and base case handling
        # dp.get(predecessor, 0) returns the length ending at predecessor, or 0 if not found.
        # Adding 1 accounts for including the current element 'x' to extend that sequence.
        current_length = dp.get(predecessor, 0) + 1
        # either finds what would be the PREVIOUS in the list, or just returns 0. Adding in the current item we are checking it against (+1) gives us the actual list val.
        
        # --- ALTERNATIVE CODE BLOCK TO .get() THAT IS LABORIOUS ---
        # # Check if the required predecessor exists in our dictionary keys
        # if predecessor in dp:
        #     # Case A: Predecessor EXISTS (Succession)
        #     # Get the length of the sequence ending at the predecessor
        #     length_of_previous = dp[predecessor]
            
        #     # The new sequence is 1 longer than the previous one
        #     current_length = length_of_previous + 1
        # else:
        #     # Case B: Predecessor DOES NOT EXIST (New Start)
        #     # The sequence starts at the current number, so its length is 1
        #     current_length = 1
        
        # Update the DP map for the current element x
        dp[x] = current_length
        
        # Update the global maximum length
        if current_length > max_length:
            max_length = current_length
            
    # The minimum length for any arithmetic sequence is 1 (the element itself).
    # We return the max length found, but at least 1 if the array wasn't empty.
    return max(1, max_length)


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findLongestArithmeticProgression(arr, k)

    print(result)
