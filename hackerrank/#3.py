# We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array. Given an array, find the maximum possible sum among  (all nonempty subarrays, all nonempty subsequences.)
# Hackerrank Link - https://www.hackerrank.com/challenges/maxsubarray/problem


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    max_so_far = -sys.maxsize
    max_subsequence = -sys.maxsize
    # stores the maximum sum of sublist ending at the current position
    max_ending_here = 0
 
    # traverse the given list
    for i in range(len(arr)):
        # update the maximum sum of sublist "ending" at index 'i' (by adding the
        # current element to maximum sum ending at previous index 'i-1')
        if arr[i] > 0:
            max_subsequence += arr[i]
        max_subsequence = max(max_subsequence, arr[i])
        
        max_ending_here = max_ending_here + arr[i]
 
        # maximum sum should be more than the current element
        max_ending_here = max(max_ending_here, arr[i])
 
        # update the result if the current sublist sum is found to be greater
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far, max_subsequence

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
