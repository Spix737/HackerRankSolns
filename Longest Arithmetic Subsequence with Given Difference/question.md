Longest Arithmetic Subsequence with Given Difference

Given an array of integers and a positive integer k, find the length of the longest arithmetic progression with common difference k. Ignore duplicates.

Example

Input

arr = [8, 1, -1, 0, 3, 6, 2, 4, 5, 7, 9]
k = 2

Output

6

Explanation

Remove duplicates (none here) and consider the set of unique elements:

We seek the longest arithmetic progression with difference k=2.

Starting at -1 gives the sequence [-1,1,3,5,7,9] of length 6.
No other starting point yields a longer progression, so the result is 6.

Input Format

    The first line contains an integer n denoting the number of elements in the array.
    The next n lines contains an integer denoting elements in the array.
    The last line contains the value for integer k.

Example

11 → number of elements
8 → elements of the array
1
-1
0
3
6
2
4
5
7
9
2 → value of k

Constraints

    0 <= arr.length <= 100000
    -10^9 <= arr[i] <= 10^9 for each 0 <= i < arr.length
    1 <= k <= 10^9
    Duplicates may appear in arr but should be ignored when forming the progression

Output Format

    A single integer denoting the length of the longest arithmetic progression.

Sample Input 0

0
5

Sample Output 0

0

Sample Input 1

1
42
7

Sample Output 1

1
