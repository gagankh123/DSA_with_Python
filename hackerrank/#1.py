# Given an amount and the denominations of coins available, determine how many ways change can be made for amount.
# Hackerrank Link - https://www.hackerrank.com/challenges/coin-change/problem


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    T = [0] * (n + 1)
    T[0] = 1
 
    for i in range(len(c)):
        j = c[i]
        while j <= n:
            T[j] += T[j - c[i]]
            j = j + 1
 
    return T[n]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
