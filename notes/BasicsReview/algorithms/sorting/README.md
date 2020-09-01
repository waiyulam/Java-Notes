
# Sorting

排序算法 | 平均时间复杂度 | 最差时间复杂度 | 空间复杂度 | 数据对象稳定性
---|---|---|---|---
[冒泡排序 Bubble Sort](#Bubble-Sort) | O(n<sup>2</sup>)|O(n<sup>2</sup>)|O(1)|稳定
[选择排序 Selection Sort](#Selection-Sort) | O(n<sup>2</sup>)|O(n<sup>2</sup>)|O(1)|数组不稳定、链表稳定
[插入排序 InsertSort](#InsertSort) | O(n<sup>2</sup>)|O(n<sup>2</sup>)|O(1)|稳定
[归并排序 MergeSort](#MergeSort) | O(n*log<sub>2</sub>n) | O(n*log<sub>2</sub>n)|O(n)|稳定
[快速排序 QuickSort](#QuickSort) | O(n*log<sub>2</sub>n) |  O(n<sup>2</sup>) | O(log<sub>2</sub>n) | 不稳定
[堆排序 HeapSort](#HeapSort) | O(n*log<sub>2</sub>n)|O(n*log<sub>2</sub>n)|O(1)|不稳定
[桶排序 BucketSort](#Bucket-sort) | O(n)|O(n)|O(m)|稳定
[希尔排序 ShellSort](https://www.geeksforgeeks.org/shellsort/) | O(n*log<sup>2</sup>n)|O(n<sup>2</sup>)|O(1)|不稳定
[计数排序 CountSort](https://www.geeksforgeeks.org/counting-sort/) | O(n+m)|O(n+m)|O(n+m)|稳定
[基数排序 RadixSort](https://www.geeksforgeeks.org/radix-sort/) | O(k*n)|O(n<sup>2</sup>)| |稳定

> * 均按从小到大排列
> * k：代表数值中的 “数位” 个数
> * n：代表数据规模
> * m：代表数据的最大值减最小值
> * 来自：[wikipedia . 排序算法](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)

## Bubble Sort

Bubble Sort is the simplest sorting algorithm that works by **repeatedly swapping the adjacent elements if they are in wrong order**.

### Examples 

```
First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

Third Pass:
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
```

### Time Complexity 

- Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

- Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

- Auxiliary Space: O(1)

- Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

- Sorting In Place: Yes

- Stable: Yes

## Selection Sort

The selection sort algorithm sorts an array by **repeatedly finding the minimum element** (considering ascending order) from unsorted part and **putting it at the beginning**.

- The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

### Implementation 
A comparison based sorting algorithm.
1. Starts with the cursor on the left, iterating left to right
2. Compares the left side to the right, looking for the smallest known item
	a. If the left is smaller than the item to the right it continues iterating
	b. If the left is bigger than the item to the right, the item on the right becomes the known smallest number
	c. Once it has checked all items, it moves the known smallest to the cursor and advances the cursor to the right and starts over
4. As the algorithm processes the data set, it builds a fully sorted left side of the data until the entire data set is sorted

Changes the array in place.

### Examples 
- In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

```
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 
``` 

### Time Complexity 

- O(n<sup>2</sup>) as there are two nested loops.

- Auxiliary Space: O(1)

- The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.

### Stability 

- A sorting algorithm is said to be **stable** if **two objects with equal or same keys appear in the same order in sorted output** as they appear in the input array to be sorted.

- The default implementation is not stable. However it can be made stable.

Selection sort works by finding the minimum element and then inserting it in its correct position by **swapping with the element which is in the position of this minimum element**. This is what makes it unstable. 

```
Note: Subscripts are only used for understanding the concept.

Input : 4A 5 3 2 4B 1
-> 1 5 3 2 4B 4A 

Output : 1 2 3 4B 4A 5

Stable Selection Sort would have produced
Output : 1 2 3 4A 4B 5
```

Swapping might impact in pushing a key(let’s say A) to a position greater than the key(let’s say B) which are equal keys. which makes them out of desired order. In the above example 4A was pushed after 4B and after complete sorting this 4A remains after this 4B. Hence resulting in unstability.

#### Stable selection sort 

Selection sort can be made Stable if instead of swapping, the **minimum element is placed in its position without swapping** i.e. by placing the number in its position by pushing every element one step forward. In simple terms use a technique like insertion sort which means inserting element in its correct place.

```
4A 5 3 2 4B 1
First minimum element is 1, now instead
of swapping. Insert 1 in its correct place 
and pushing every element one step forward
i.e forward pushing.
1 4A 5 3 2 4B
Next minimum is 2 :
1 2 4A 5 3 4B
Next minimum is 3 :
1 2 3 4A 5 4B
Repeat the steps until array is sorted.
1 2 3 4A 4B 5
```

## Insert Sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

To sort an array of size n in ascending order:

1. Iterate from arr[1] to arr[n] over the array.
2. Compare the current element (key) to its predecessor.
3. If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

<p align="center">
<img width="300" height="300" src= "https://media.geeksforgeeks.org/wp-content/uploads/insertionsort.png">
</p>

### Visualization 

<p align="center">
<img width="400" height="200" src= "https://camo.githubusercontent.com/8f6fedc10da579f13b22b949f6ad29255b6d721f/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f302f30662f496e73657274696f6e2d736f72742d6578616d706c652d33303070782e676966">
</p>

### Time complexity 

- Time Complexity: O(n*2)

Although it has an O(n^2), in practice it slightly less since its comparison scheme only requires checking place if its smaller than its neighbor.

- Auxiliary Space: O(1)

- Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.

- Sorting In Place: Yes

- Stable: Yes

### Uses 

Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.

### Implementation : linked list 

1) Create an empty sorted (or result) list
2) Traverse the given list, do following for every node.
	a) Insert current node in sorted way in sorted or result list.
3) Change head of given linked list to head of sorted (or result) list. 

> NOTE: Implement insertion sort as array/list is expensive because you need to create room for inserted element and "scooting over" all the element on the right 


## [Merge sort](https://www.geeksforgeeks.org/merge-sort/)

Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See following C implementation for details.

1. Recursively divides entire array by half into subsets until the subset is one, the base case.
2. Once the base case is reached results are returned and sorted ascending left to right.
3. Recursive calls are returned and the sorts double in size until the entire array is sorted.

```
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
```

<p align="center">
<img width="300" height="500" src="https://camo.githubusercontent.com/8789a4a0ed51a843aafe679323bfa25a37fd1395/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f652f65362f4d657267655f736f72745f616c676f726974686d5f6469616772616d2e7376672f34303070782d4d657267655f736f72745f616c676f726974686d5f6469616772616d2e7376672e706e67">
</p >

### Time complexity 

Time complexity of Merge Sort is O(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and take linear time to merge two halves.

- Auxiliary Space: O(n)

- Sorting In Place: No in a typical implementation

- Stable: Yes


## [QuickSort](https://www.geeksforgeeks.org/quick-sort/)

QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. 

- Partitions entire data set in half by selecting a random pivot element and putting all smaller elements to the left of the element and larger ones to the right.
- It repeats this process on the left side until it is comparing only two elements at which point the left side is sorted.
- When the left side is finished sorting it performs the same operation on the right side.

### Pivot 

1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. **Pick a random element as pivot.**
4. Pick median as pivot.

### Partition 

Given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time O(n).

we start from the leftmost element and keep track of index of smaller (or equal to) elements as i. While traversing, if we find a smaller element, we swap current element with arr[i]. Otherwise we ignore current element.

```java
/* This function takes last element as pivot, places
   the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
   to left of pivot and all greater elements to right
   of pivot */
	partition (arr[], low, high)
	{
		// pivot (Element to be placed at right position)
		pivot = arr[high];  
	
		i = (low - 1)  // Index of smaller element

		for (j = low; j <= high- 1; j++)
		{
			// If current element is smaller than the pivot
			if (arr[j] < pivot)
			{
				i++;    // increment index of smaller element
				swap arr[i] and arr[j]
			}
		}
		swap arr[i + 1] and arr[high])
		return (i + 1)
	}
```
#### Example
```java 

arr[] = {10, 80, 30, 90, 40, 50, 70}
Indexes:  0   1   2   3   4   5   6 

low = 0, high =  6, pivot = arr[h] = 70
Initialize index of smaller element, i = -1

Traverse elements from j = low to high-1
j = 0 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 0 
arr[] = {10, 80, 30, 90, 40, 50, 70} // No change as i and j 
                                     // are same

j = 1 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 2 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 1
arr[] = {10, 30, 80, 90, 40, 50, 70} // We swap 80 and 30 

j = 3 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 4 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 2
arr[] = {10, 30, 40, 90, 80, 50, 70} // 80 and 40 Swapped
j = 5 : Since arr[j] <= pivot, do i++ and swap arr[i] with arr[j] 
i = 3 
arr[] = {10, 30, 40, 50, 80, 90, 70} // 90 and 50 Swapped 

We come out of loop because j is now equal to high-1.
Finally we place pivot at correct position by swapping
arr[i+1] and arr[high] (or pivot) 
arr[] = {10, 30, 40, 50, 70, 90, 80} // 80 and 70 Swapped 

Now 70 is at its correct place. All elements smaller than
70 are before it and all elements greater than 70 are after
it.

```

### Implementation 

``` java 
/* low  --> Starting index,  high  --> Ending index */
	quickSort(arr[], low, high)
	{
		if (low < high)
		{
			/* pi is partitioning index, arr[pi] is now
			at right place */
			pi = partition(arr, low, high);

			quickSort(arr, low, pi - 1);  // Before pi
			quickSort(arr, pi + 1, high); // After pi
		}
	}
``` 

### Example: choose last element as pivot 

<p align="center">
<img width="500" height="300" src= "https://www.geeksforgeeks.org/wp-content/uploads/gq/2014/01/QuickSort2.png">
</p>

### Visualization 

<p align="center">
<img width="300" height="300" src= "https://camo.githubusercontent.com/2499d89bbb30337a5d2d7770cc034b4b71fbfdc6/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f362f36612f536f7274696e675f717569636b736f72745f616e696d2e676966">
</p>

### Time Complexity 

- **Worst Case:** The worst case occurs when the partition process always **picks greatest or smallest element as pivot**. If we consider above partition strategy where last element is always picked as pivot, the worst case would occur when the array is already sorted in increasing or decreasing order which turns out in O(n<sup>2</sup>)

- **Best Case**: The best case occurs when the partition process **always picks the middle element as pivot**. Following is recurrence for best case.

>  T(n) = 2T(n/2) + O(n)

The solution of above recurrence is O(nLogn). 

### Merge Sort Vs. Quicksort

Although the worst case time complexity of QuickSort is O(n<sup>2</sup>) which is more than many other sorting algorithms like Merge Sort and Heap Sort, QuickSort is faster in practice, because its **inner loop can be efficiently implemented on most architectures**, and in most real-world data. QuickSort can be implemented in different ways by changing the choice of pivot, so that the worst case rarely occurs for a given type of data. However, merge sort is generally considered better when data is huge and stored in external storage.

- Merge Sort divides the set into the smallest possible groups immediately then reconstructs the incrementally as it sorts the groupings.

- Quicksort continually partitions the data set by a pivot, until the set is recursively sorted.

#### Why Quick Sort is preferred over MergeSort for sorting Arrays

- Quick Sort in its general form is an in-place sort (i.e. it doesn’t require any extra storage) whereas merge sort requires O(N) extra storage, N denoting the array size which may be quite expensive. Allocating and de-allocating the extra space used for merge sort increases the running time of the algorithm. Comparing average complexity we find that both type of sorts have O(NlogN) average complexity but the constants differ. **For arrays, merge sort loses due to the use of extra O(N) storage space.**

- Quick Sort is also a **cache friendly sorting algorithm** as it has good locality of reference when used for arrays.

- **Quick Sort is also tail recursive, therefore tail call optimizations is done.**

#### Why MergeSort is preferred over QuickSort for Linked Lists?

- In case of linked lists the case is different mainly due to difference in **memory allocation of arrays and linked lists**. Unlike arrays, linked list nodes may not be adjacent in memory. Unlike array, in linked list, **we can insert items in the middle in O(1) extra space and O(1) time**. Therefore **merge operation of merge sort can be implemented without extra space for linked lists**.

- In arrays, we can do random access as elements are continuous in memory. Let us say we have an integer (4-byte) array A and let the address of A[0] be x then to access A[i], we can directly access the memory at (x + i*4). **Unlike arrays, we can not do random access in linked list**. **Quick Sort requires a lot of this kind of access**. **In linked list to access i’th index, we have to travel each and every node from the head to i’th node as we don’t have continuous block of memory**. Therefore, the overhead increases for quick sort. **Merge sort accesses data sequentially and the need of random access is low**.

### Stability 

The default implementation is not stable. However any sorting algorithm can be made stable by considering indexes as comparison parameter.

### In place 

Quick Sort in its general form is an in-place sort (i.e. it doesn’t require any extra storage) as it uses extra space only for storing recursive function calls but not for manipulating the input.


## HeapSort

1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of tree.
3. Repeat above steps while size of heap is greater than 1.

### Heapify 

Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom up order.

```
Input data: 4, 10, 3, 5, 1
         4(0)
        /   \
     10(1)   3(2)
    /   \
 5(3)    1(4)

The numbers in bracket represent the indices in the array 
representation of data.

Applying heapify procedure to index 1:
         4(0)
        /   \
    10(1)    3(2)
    /   \
5(3)    1(4)

Applying heapify procedure to index 0:
        10(0)
        /  \
     5(1)  3(2)
    /   \
 4(3)    1(4)
The heapify procedure calls itself recursively to build heap
 in top down manner.
 ```

 ### Time complexity 
 Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n) and overall time complexity of Heap Sort is O(nLogn).

 - Heap sort is an in-place algorithm.	
 - Its typical implementation is not stable, but can be made stable

Heap sort algorithm has limited uses because Quicksort and Mergesort are better in practice. 

## [Bucket sort](https://www.geeksforgeeks.org/bucket-sort-2/)

Bucket sort is mainly useful when input is uniformly distributed over a range. For example, consider the following problem.

```
Sort a large set of floating point numbers which are in range from 0.0 to 1.0
and are uniformly distributed across the range. How do we sort the numbers
efficiently?
```

### Implementation 
bucketSort(arr[], n)
1) Create n empty buckets (Or lists).
2) Do following for every array element arr[i].
	a) Insert arr[i] into bucket[n*array[i]]
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.

<p>
<img width="400" height="300" src="https://media.geeksforgeeks.org/wp-content/uploads/BucketSort.png">
</p>

# Time complexity 
 If we assume that insertion in a bucket takes O(1) time then steps 1 and 2 of the above algorithm clearly take O(n) time. The O(1) is easily possible if we use a linked list to represent a bucket (In the following code, C++ vector is used for simplicity). Step 4 also takes O(n) time as there will be n items in all buckets.
The main step to analyze is step 3. This step also takes O(n) time on average if all numbers are uniformly distributed 


![](https://res.cloudinary.com/practicaldev/image/fetch/s--POn2iYyz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://cdn-images-1.medium.com/max/1600/1%2AbPpvELo9_QqQsDz7CSbwXQ.gif) 