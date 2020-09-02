
# [Static Arrays](https://www.interviewcake.com/concept/python/array?)

## Definition 
- A static array is a fixed length container containing n elements **indexable** from range [0,n-1]
- **Indexable**: each slot/index in the array can be referenced with a number 

## Uses
1. Storing and accessing sequential data 
2. Temporaritly storing objects 
3. Used by IO routines as buffers 
4. Lookup tables and inverse lookup tables 
5. Used as multiple values return or args input from a function 
6. Used in DP to cache ansers to subproblems 

## Strengths
- **Fast lookups**: Retrieving the element at a given index takes O(1) time, regardless of the length of the array.

## Weaknesses
- **Fixed size**: You need to specify how many elements you're going to store in your array ahead of time. (Unless you're using a fancy dynamic array.)
- **Costly inserts and deletes**: You have to "scoot over" the other elements to fill in or close gaps, which takes worst-case O(n) time.

## Declaration : java 
```java
 int gasPrices[] = new int[10];

gasPrices[0] = 346;
gasPrices[1] = 360;
gasPrices[2] = 354;
```

## Time Complexity 

Ops|Average Case|Worst Case 
---|---|---|
Space|O(n)|O(n)
Access|O(1)|O(1)
Appending|N/A|N/A
Insertion|N/A|N/A
Deletion|N/A|N/



# [Dynamic Arrays](https://www.interviewcake.com/concept/python/dynamic-array)

## Definition 

- **Automatic Resizing**: like one dimensional arrays, but have **reserved space for additional elements**. If a dynamic array is full, it **copies its contents to a larger array.**

## Strengths

- **Fast lookups** :Just like arrays, retrieving the element at a given index takes O(1)O(1) time.
- **Variable size**: You can add as many items as you want, and the dynamic array will expand to hold them.
- **Cache-friendly**: Just like arrays, dynamic arrays place items right next to each other in memory, making efficient use of caches.

## Weaknesses

- **Slow worst-case appends**: Usually, adding a new element at the end of the dynamic array takes O(1)O(1) time. But if the dynamic array doesn't have any room for the new item, it'll need to expand(copy all the elements and double size of array), which takes O(n) time.
- **Costly inserts and deletes**: Just like arrays, elements are stored adjacent to each other. So adding or removing an item in the middle of the array requires "scooting over" other elements, which takes O(n) time.

## Implementation : Python 
```python 
# In Python, dynamic arrays are called lists.
gas_prices = []

gas_prices.append(346)
gas_prices.append(360)
gas_prices.append(354)
```

## Notes 

### Size v.s Capacity 
![](https://www.interviewcake.com/images/svgs/dynamic_arrays__capacity_size_end_index.svg?bust=206)     

We'd say this dynamic array's size is 4 and its capacity is 10. The dynamic array stores an end_index to keep track of where the dynamic array ends and the extra capacity begins.

### Doubling Space 
What if we try to append an item but our array's capacity is already full?<br>
To make room, dynamic arrays automatically make a new, bigger underlying array. Usually twice as big. and each item has to be individually copied into the new array.

> Notes: Why not just extend the existing array? Because that memory might already be taken by another program.


## Time Complexity

Ops|Average Case|Worst Case 
---|---|---|
Space|O(n)|O(n)
Access|O(1)|O(1)
Appending|O(1)|O(n)
Insertion|O(n)|O(n)
Deletion|O(n)|O(n)