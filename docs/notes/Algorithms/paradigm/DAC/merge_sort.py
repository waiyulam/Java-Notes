#!/bin/python 
import sys
import random 

def merge(arr,m,l,r):
    A = [arr[i] for i in range(l,m+1)]
    B = [arr[i] for i in range(m+1,r+1)]
     # 2-way merging 
    i = 0
    j = 0
    k = l
    while ( i<len(A) and j <len(B)):
        if (A[i] > B[j]):
            arr[k] = B[j]
            k += 1 
            j += 1 
        else:
            arr[k] = A[i]
            k += 1 
            i += 1 
    # Copy the rest of elements 
    while (i<len(A)):
        arr[k] = A[i]
        k += 1 
        i += 1
    while (j<len(B)):
        arr[k] = B[j]
        k += 1
        j += 1 

def mergeSort(arr,l,r): 
    if (l<r):
        mid = (l+r) // 2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,mid,l,r)

if __name__ == "__main__":
    # Driver code to test above 
    arr = [random.randint(0,1000) for i in range(0,1000)]
    temp = arr.copy()
    temp.sort()
    n = len(arr) 
    print ("Given array is {}".format(arr)) 
    
    # DAC
    mergeSort(arr,0,len(arr)-1) 
    if (temp == arr):
        print ("Sorted array is {}".format(arr)) 
