#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    
    # empty input edge case (could be type safe too)
    if not intervals:
        return []

    # sort those intervals!
    intervals.sort(key=lambda x: x[0])

        
    # get 1st interval, call it merged
    merged = [intervals[0]]
    
    # for every OTHER interval:
    for current_start, current_end in intervals[1:]:
        # get our merge's start and end
        last_merged_start, last_merged_end = merged[-1]
        
        # if the start of the one we're checking is less than the end of the 'merge':
        # e.g. [1,6] & [2,3] = 2 < 6 True so
        if current_start <= last_merged_end:
            # we "merge" it and keep the biggest ender => max(6,3) = 6
            merged[-1][1] = max(last_merged_end, current_end)
            # we only need to check for max because thanks to sort our last_merged_min is always actual min!
        else:
            merged.append([current_start, current_end])
            
    return merged
        
            
    
    

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
