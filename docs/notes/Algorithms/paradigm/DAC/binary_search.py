#!/bin/python 
import sys 
import time

def binary_search(A,n,key):
    # lens of list A 
    l = 0
    h = n - 1
    while(l <= h):
        mid = (l+h) // 2
        if (A[mid] == key):
            return mid
        elif (A[mid] > key):
            h = mid - 1
        else:
            l = mid + 1
    return -1

# Recursive method 
def bs_dac(l,h,key):
    if (l > h):
        return -1
    mid = (l + h) // 2
    if (A[mid] == key):
        return mid
    elif (A[mid] > key):
        return bs_dac(l,mid-1,key)
    else:
        return bs_dac(mid+1,h,key)


if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9,10,11]
    key = int(input("Please enter your key you are searching: "))
    if(binary_search(A,len(A),key) != -1):
        print("Key {} was found!".format(key))
    else:
        print("Key not found.")
    
    if(bs_dac(0,len(A)-1,key) != -1 ):
        print("Key {} was found!".format(key))
    else:
        print("Key not found.")
