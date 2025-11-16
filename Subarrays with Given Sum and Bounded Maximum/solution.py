#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countSubarraysWithSumAndMaxAtMost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. LONG_INTEGER k
#  3. LONG_INTEGER M
#

def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    """
    Count all contiguous subarrays whose:
      - sum equals k
      - maximum element is <= M

    Optimal strategy:
      1. Any element > M immediately invalidates a subarray.
      2. Therefore, split the array into segments separated by elements > M.
      3. Within each segment, count subarrays whose sum = k using prefix sums.
    """

    total = 0
    segment = []

    for x in nums:
        if x > M:
            # Element too large. It breaks all contiguous subarrays.
            # Process the completed segment and reset it.
            total += count_subarrays_with_sum(segment, k)
            segment = []
        else:
            # Build a segment containing only values <= M.
            segment.append(x)

    # Process the last segment after finishing the scan.
    total += count_subarrays_with_sum(segment, k)

    return total


def count_subarrays_with_sum(arr, k):
    """
    Count subarrays within 'arr' whose sum is exactly k.
    Uses the classic prefix-sum frequency dictionary.

    Explanation (deep this; it's rudimentarily simple. Once you get it it's genius and simple):
      prefix[i] = sum(arr[0..i])

      A subarray (i..j) has sum k if:

         prefix[j] - prefix[i-1] = k

      which is the same as:

         prefix[i-1] = prefix[j] - k

      So for each position j, we look up how many times the value
      (prefix[j] - k) has appeared before.
    """

    prefix_counts = {0: 1}  # prefix sum 0 has appeared once (empty prefix)
    prefix = 0              # running prefix sum
    count = 0               # total valid subarrays found

    for x in arr:
        prefix += x

        needed = prefix - k  # the prefix value needed for a match

        # If needed prefix values were seen before, they form valid subarrays.
        if needed in prefix_counts:
            count += prefix_counts[needed]

        # Record the current prefix value.
        prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1

    return count

        

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    k = int(input().strip())

    M = int(input().strip())

    result = countSubarraysWithSumAndMaxAtMost(nums, k, M)

    print(result)
