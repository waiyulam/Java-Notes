#!/bin/python 
import sys
import time 
# Albert : iteration solution 
# Fibonacci_cache = {}
Fibonacci_cache = {}

def Fib_A(n):
    if n <= 1: 
        return n
    f1 = 0
    f2 = 1
    result = 0
    for i in range(2,n+1):
        result = f1 + f2
        f1 = f2 
        f2 = result 
    return result 


# Pinto : recursive solution 
def Fib_P(n): 
    if n <= 1:
        return n 
    return Fib_P(n-1) + Fib_P(n-2)

# Pinto with memoization 
def Fib_M(n):
    if n<=1:
        return n 
    elif n in Fibonacci_cache:
        return Fibonacci_cache[n]
    Fibonacci_cache[n] = Fib_M(n-1) + Fib_M(n-2) 
    return Fibonacci_cache[n] 

if __name__ == "__main__":
    n = int(input("Give me a n : "))
    start = time.time()
    print("The Fibonacci number {} is {} ".format(n,Fib_P(n)))
    end = time.time()
    print("Total time : {}".format(end-start))
    #Implement recursive function with memoization 
    start = time.time()
    print("The Fibonacci number w/ memoization {} is {} ".format(n,Fib_M(n)))
    end = time.time()
    print("Total time w/ memoization : {}".format(end-start))