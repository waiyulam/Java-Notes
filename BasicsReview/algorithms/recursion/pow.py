#!/bin/python 
import sys 
import time

# O(n) solution  
def pow_albert(x,n):
    if n == 0:
        return 1 
    return x * pow_albert(x,n-1)

# O(log(n)) solution 
def pow_pinto(x,n):
    if n == 0:
        return 1 
    elif n%2 == 0:
        res = pow(x,n/2)
        return res * res 
    return x * pow_pinto(x,n-1)

if __name__ == "__main__":
    x = int(input("Please enter the base number : "))
    n = int(input("Please enter the order number : "))
    start = time.time()
    res = pow_albert(x,n)
    end = time.time()
    print("The {} to the power of {} is equal to {}. \n Total time taken by albert is : {}".format(x,n,res,end-start))
    start = time.time()
    res = pow_pinto(x,n)
    end = time.time()
    print("The {} to the power of {} is equal to {}. \n Total time taken by pinto is : {}".format(x,n,res,end-start))
