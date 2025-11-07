#!/bin/python3

import math
import os
import random
import re
import sys




#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(response_times):
    # 1. Handle edge cases: The list must have at least 2 elements to compare the second
    #    with the average of the first (which is just the first).
    if len(response_times) < 2:
        return 0
    
    count = 0
    cum_sum = response_times[0]
        
    for i, current_rt in enumerate(response_times[1:], start=1):
            
        # explicit cast to float to ensure division yields a float; avoiding potential integer truncation err.
        previous_average = cum_sum / float(i)
        
        # The condition: strictly greater
        if current_rt > previous_average:
            count += 1
            
        # Update cum_sum for the next iteration
        cum_sum += current_rt

    return count





if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
