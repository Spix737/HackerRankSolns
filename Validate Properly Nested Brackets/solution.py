#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
    stack = []
    
    # Define the mapping of closing brackets to their required opening partners
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Define sets for quick lookups
    openers = set(bracket_map.values()) # { '(', '[', '{' }
    closers = set(bracket_map.keys())   # { ')', ']', '}' }

    for char in code_snippet:
        if char in openers:
            # If it's an opening bracket, push it onto the stack.
            stack.append(char)
        
        elif char in closers:
            # If it's a closing bracket:
            
            if not stack:
                return 0
            
            # 2. Pop the most recent opening bracket.
            most_recent_opener = stack.pop()
            
            # 3. Check if the popped opener matches the current closer's requirement.
            # E.g., if char is ')', bracket_map[char] is '('.
            if most_recent_opener != bracket_map[char]:
                # Mismatch found (e.g., received ')' but stack had '[')
                return 0
    
    # stack also needs to be empty at the end, all brackets closed
    return 1 if not stack else 0
            
        
    
    
    

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
