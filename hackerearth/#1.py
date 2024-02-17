'''
Problem:

You are given an array  of  integers. You want to choose some integers from the array subject to the condition that the number of distinct integers chosen should not exceed . Your task is to maximize the sum of chosen numbers.

You are given  test cases.

Input format

The first line contains a single integer  denoting the number of test cases.
The first line of each test case contains two space-separated integers  and  denoting the length of the array and the maximum number of distinct integers you can choose.
The second line of each test case contains  space-separated integers denoting the integer array .
Output format

For each test case(in a separate line), print the maximum sum you can obtain by choosing some elements such that the number of distinct integers chosen is at most . If you cannot choose any element, output .
'''

def user_input():
    '''

    T as number of test cases
    N as Length of List & K as Number of distinct elements
    A as list of length N

    :return: N, K, A
    :rtype: int, int, list
    '''

    T = int(input())
    for counter in range(T):
        N, K = [int(x) for x in input().split()]
        A = [int(i) for i in input().split()]

        if len(A) != N:
            raise Exception("Invalid Input List. N is not matching with List Length.")

        yield N, K, A

def maximize_the_sum(K, A):
    sum_dict = {}
    for i in A:
        sum_dict[i] = i if i not in sum_dict else i + sum_dict[i]

    sort_sum = sorted(sum_dict.values(), reverse=True)
    sort_sum = [i if i>0 else 0 for i in sort_sum]
    return sum(sort_sum[:K])

if __name__ == "__main__":
    user_inp = user_input()  # taking user input for each test case.

    for N, K, A in user_inp:
        output = maximize_the_sum(K, A)
        print(0 if output is None else output)