#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestSubstringWindow' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY patterns
#  2. STRING S
#

def findSmallestSubstringWindow(patterns, S):
    # Step 0: Quick edge case check
    if not S or not patterns:
        return [-1, -1]

    intervals = []            # Will store (start, end, pattern_id)
    
    # Step 1: Find all occurrences (intervals) of each pattern
    for pid, pattern in enumerate(patterns):
        plen = len(pattern)
        for i in range(len(S) - plen + 1):  # optimal, searching exactly only valid space
            if S[i:i + plen] == pattern:    # you can check splits... and it's optimized by python presumably
                intervals.append((i, i + plen - 1, pid))

    # If any pattern has no intervals, solution is impossible
    if not intervals:
        return [-1, -1]

    num_patterns = len(patterns)
    intervals.sort(key=lambda x: x[0])  # Sort by start position

    # Step 2: Sliding window on the intervals
    left = 0
    pattern_count = {pid: 0 for pid in range(num_patterns)}  # Track how many active intervals (currently inside window) per pattern ID. If >0, that pattern is "covered"
    covered_patterns = 0     # How many distinct patterns currently covered
    best = (float('inf'), -1, -1)  # (window_size, start, end)

    for right in range(len(intervals)):
        start_r, end_r, pid_r = intervals[right]
        # Include this interval
        if pattern_count[pid_r] == 0:
        # We've "added" this interval to our window now
            # This is the first occurrence of this pattern inside the current window
            # so we now cover one more unique pattern.
            covered_patterns += 1
        pattern_count[pid_r] += 1
        # Increase count of this pattern's intervals currently inside window.
        # If multiple overlapping intervals for same pattern are inside window,
        # this avoids "losing" the pattern when we remove just one later.

        # When all patterns are covered, try to shrink window from the left
        while covered_patterns == num_patterns and left <= right:
            start_l, end_l, pid_l = intervals[left]     # window and id all-in-1
            # This is the interval we may try to remove next
            # Window spans from min start (left) to max end (right)
            
            window_start = intervals[left][0]
            # Start of window = start index of *left-most interval*
            
            window_end = max(iv[1] for iv in intervals[left:right + 1])
            # End of window = max end index across all intervals inside window
            # Note: must compute since intervals inside may extend beyond current `right`.


            window_size = window_end - window_start + 1
            # Actual substring length

            # If this window is better, store it
            if window_size < best[0]:
                best = (window_size, window_start, window_end)

            # Now attempt to shrink window: remove interval at 'left'
            pattern_count[pid_l] -= 1
            # Reduce count of that pattern

            if pattern_count[pid_l] == 0:
                # That pattern is no longer fully covered, so we decrement
                covered_patterns -= 1
                
            left += 1
            # Move left pointer forward to shrink window

    if best[1] == -1:
        return [-1, -1]
    return [best[1], best[2]]

        
        
    
    
    # Write your code here

if __name__ == '__main__':
    patterns_count = int(input().strip())

    patterns = []

    for _ in range(patterns_count):
        patterns_item = input()
        patterns.append(patterns_item)

    S = input()

    result = findSmallestSubstringWindow(patterns, S)

    print('\n'.join(map(str, result)))
