#!/bin/python
import sys 
import random
# the pivot point is fixed in array for each iteration 
# the left end and right end elements is fixed 
# we need one extra space on the right end because we fixed the left end 
def partition(arr,l,h):
    # pick middle element as pivot point 
    mid = (l+h)//2
    pivot = arr[mid]
    # Move pivot element to the left end in array for indexing problem 
    arr[l],arr[mid] = arr[mid],arr[l]
    i = l+1
    for j in range(l+1,h+1):
        # If current element is smaller than pivot 
        if (arr[j] < pivot):
            arr[j],arr[i] = arr[i],arr[j]
            # increment smaller index 
            i += 1
    arr[l],arr[i-1] = arr[i-1],arr[l]
    return i-1


def quicksort(arr,l,h):
    if l<h:
        p = partition(arr,l,h)
        quicksort(arr,l,p)
        quicksort(arr,p+1,h)

if __name__ == "__main__":
    # Driver code to test above 
    arr = [random.randint(0,100) for i in range(0,100)]
    # arr = [2,4,5,3,9]
    temp = arr.copy()
    temp.sort()
    n = len(arr) 
    print ("Given array is {}".format(arr)) 
    
    # DAC
    quicksort(arr,0,n-1) 
    if (temp == arr):
        print ("Sorted array is {}".format(arr)) 

