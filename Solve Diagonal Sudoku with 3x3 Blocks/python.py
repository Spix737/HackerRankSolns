#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'completeDiagonalSudokuGrid' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def completeDiagonalSudokuGrid(grid):
    # This soln uses uses backtracking.
    N = 9

    # Validates placing val at (r(ow), c(olumn)) [think of as 3x3 grid coordinates]
    def is_valid(r, c, val):
        # Row
        if any(grid[r][j] == val for j in range(N)):
            return False
        # Column
        if any(grid[i][c] == val for i in range(N)):
            return False
        # 3x3 block
        br = (r // 3) * 3
        bc = (c // 3) * 3
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if grid[i][j] == val:
                    return False
        # Main diagonal
        if r == c:
            if any(grid[i][i] == val for i in range(N)):
                return False
        # Anti-diagonal
        if r + c == N - 1:
            if any(grid[i][N - 1 - i] == val for i in range(N)):
                return False
        return True

    # Searches for next empty cell (0)
    def find_empty():
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    return i, j
        return None

    # the juice - Recursive Backtracking Core
    def backtrack():
        pos = find_empty()
        if not pos:
            return True  # solved

        r, c = pos

        # Try digits 1-9
        for val in range(1, 10):
            if is_valid(r, c, val):
                grid[r][c] = val  # Tentatively place
                if backtrack(): # Recurse
                    return True
                grid[r][c] = 0  # undo on failure
        return False

    # begin recursion (main)
    backtrack()
    return grid


if __name__ == '__main__':
    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = completeDiagonalSudokuGrid(grid)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
