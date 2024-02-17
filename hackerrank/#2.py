# Determine the sum of all integer values of substrings of the string. Given an integer as a string, sum all of its substrings cast as integers.
# Hackerrank Link - https://www.hackerrank.com/challenges/sam-and-substrings/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(inp):
    num = list(inp)
    n = len(num)

    # storing prev value
    prev = int(num[0])
 
    res = prev  # ans
 
    current = 0
 
    # substrings sum upto current index
    # loop over all digits of string
    for i in range(1, n):
        numi = int(num[i])
 
        # update each sumofdigit from previous value
        current = (i + 1) * numi + 10 * prev
 
        # add current value to the result
        res += current
        prev = current  # update previous
 
    return res % 1000000007
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inp = input()

    result = substrings(inp)

    fptr.write(str(result) + '\n')

    fptr.close()





# ========= Solution 2 ===========
import operator

MOD = 1000000007

s = input()
n = len(s)
a = []
p10 = 0
for i in range(n, 0, -1):
	p10 = (p10 * 10 + 1) % MOD
	a.append(p10 * i % MOD)

b = [ord(c) - ord('0') for c in s]
print(sum(map(operator.mul, reversed(a), b)) % MOD)