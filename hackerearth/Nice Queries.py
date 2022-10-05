'''
Problem:

You are given an array A of length N which is initialised with 0. You will be given Q queries of two types:

: set value 1 at index k in array A

: print the smallest index x which is greater than or equal to y and having value 1. If there is no such index print -1.

Note: Indexing is 1 based

Input Format

First line contains two integers N and Q separated by a space.

The next Q lines contain the type of query (i.e. either a 1 or a 2), then a space, then for type 1 queries integer k and for type 2 queries integer y

Output Format

For each query type 2, print in new line, the smallest index x which is greater than or equal to y and having value 1. If there is no such index print -1.
'''

def user_input():
    '''

    N as list length and Q as Number of queries
    T as query type and index as K/Y

    :return: A (0th list of N length), queries array
    :rtype: list, list
    '''

    N, Q = [int(x) for x in input().split()]
    A = [0]*N
    queries = []
    for query in range(Q):
        # queries.append([int(x) for x in input().split()])
        T, index = [int(x) for x in input().split()]
        if T == 1:
            A[index-1] = 1
        elif T == 2:
            sub_array = A[index-1:]
            if 1 in sub_array:
                print(sub_array.index(1) + index)
            else:
                print(-1)
    # return A, queries

def nice_query():

    for T, index in queries:
        if T == 1:
            A[index-1] = 1
        elif T == 2:
            sub_array = A[index-1:]
            if 1 in sub_array:
                print(sub_array.index(1) + index)
            else:
                print(-1)

if __name__ == "__main__":
    user_input()