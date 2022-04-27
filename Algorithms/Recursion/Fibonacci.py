# Given a number N return the index value of the Fibonacci
# sequence, where the sequence is:
# 0,1,1,2,3,5,8,13,21,34,55,89,144...
# the pattern of the sequence is that each value is the sum of 
# the 2 previous values, that means that for N=5 -> 2+3

# For bigo recursive is very bad
# Anything we do with recursive can be done with iterative as well
# DRY             Large Stack
# Readable
# https://2ality.com/2015/06/tail-call-optimization.html
# Tail call optimization allows us to create recursive functions without increasing the call stack

# Every time we are using a tree or converting something into a tree, consider recursion
# 1-Divided into a number of subproblems that are smaller instances of the same problem
# 2-Each instance of the subproblem is identical in nature.
# 3-The solutions of each subproblem can be combined to solve the problem at hand
# Divide and Conquer using Recursion

def fibonacciRecursive(n): #O(2^N) # exponential time, size of tree exponentially grows when and increases
    if n < 2:
        return n

    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

print(fibonacciRecursive(8))

def fibonacciIterative(n): #O(n)
    if n < 2:
        return n
    
    temp = 0
    pointer = 2
    currentNum = 2
    previousNum = 1
    while pointer < n - 1:
        temp = currentNum + previousNum
        previousNum = currentNum
        currentNum = temp
        pointer += 1
    
    return temp

def fibonacciIterative2(n):
    arr = [0,1]
    for i in range(2,n+1):
        arr.append(arr[i-2] + arr[i-1])

    return arr[n]


print(fibonacciIterative2(8))
print(fibonacciIterative(8))
