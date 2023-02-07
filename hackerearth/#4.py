# Candy in the box
# Link - https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/candy-in-the-box-75b63839/

'''
solution: 
1. If N >= K then output is K as we can put K candies in K boxes.
2. Else from 2nd round onwards, only 9 boxes left for candies to put in. Even iteration starts from right and odd iteration starts from left. 
'''

import math
testcase = int(input())

while(testcase):
    testcase -= 1
    N, K = (int(i) for i in input().split())

    if K<=N:
        print(K)
    else:
        K -= N
        div = math.floor(K/(N-1))
        rem = K%(N-1)
        if div%2==0:
            print(N-rem)
        else:
            print(rem+1)

