# Velocities of balls
# Link - https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/bouncing-balls-b9c19a3d/

'''
solution: 
1. find all collision index (make sure same collision index not come twice.)
    Approach - iterate balls from left to right and find the ball (with positive velocity) which collide with a higher position ball which has negative velocity. 
2. Sort all collision based on time. Faster collision will be on top. d1*t2 - d2*t1
3. For each collision, calculate time and add time to the current position index. Swap position index after collision. 

'''

import functools
import math
 
testcase = int(input())
 
while(testcase):
    testcase -=1
    balls  = int(input())
    position = [int(i) for i in input().split()]
    velocity = [int(i) for i in input().split()]
    
 
    hit = []
 
    for i in range(balls):
        for j in range(balls):
            if(position[i]<position[j] and velocity[i]>0 and velocity[j]<0):
                hit.append((i,j))
    
    def compare(x,y):
        return ((position[x[1]] - position[x[0]])*(velocity[y[0]] - velocity[y[1]]) ) - ((position[y[1]] - position[y[0]])*(velocity[x[0]] - velocity[x[1]]))
    # print(hit)
    hit = sorted(hit,key=functools.cmp_to_key(compare))
    # print(hit)
    ans = [0 for _ in range(balls)]
    curr = [i for i in range(balls)]
 
    for i in hit:
        time = math.floor((position[i[1]]-position[i[0]])/(velocity[i[0]]-velocity[i[1]]))
        ans[curr[i[0]]] +=time
        ans[curr[i[1]]] +=time
        temp = curr[i[0]]
        curr[i[0]] = curr[i[1]]
        curr[i[1]] = temp
 
 
    for i in ans:
        print(i)