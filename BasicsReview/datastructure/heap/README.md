# Binary Heap

## Definition

- A binary heap is a **binary tree** where the **smallest value** is always at the **top**

<p align="center">
<img weight="300" height="200" src="https://www.geeksforgeeks.org/wp-content/uploads/MinHeapAndMaxHeap.png">
</p>

### Types 

- **Max Heap**: the key present at the root node must be greatest among the keys presented at all of its children. **The same property must be recursively true for all sub trees in that Binary Tree**

- **Min Heap**: the key present at the root node must be minimum among the keys presented at all of its children. **The same property must be recursively true for all sub trees in that Binary Tree**

## Uses

- **Priority queues**: implemented using heaps. Items are enqueued by adding them to the heap, and the highest-priority item can quickly be grabbed from the top.
- **Heap sort**: make a heap out of them and then remove items one at a time—in sorted order.

## Implementation 
- Heaps are implemented as **complete binary trees**.

> In a complete binary tree:
> - each level is filled up before another level is added
> - the bottom tier is filled in from left to right.  
> As we'll see, this allows us to efficiently store our heap as a list.

- In a heap, **every node is smaller than its children**.
<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap__binary_tree_with_comparing_node_1_and_lower_level.svg?bust=206">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap__binary_tree_with_comparing_node_5_and_lower_level.svg?bust=206">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap__binary_tree_with_comparing_node_2_and_lower_level.svg?bust=206">
</p>



## Strengths:
- **Quickly access the smallest item**: Binary heaps allow you to grab the smallest item (the root) in O(1) time, while keeping other operations relatively cheap (O(lg(n)) time).
- **Space efficient**: Binary heaps are usually implemented with **lists**, saving the overhead cost of storing pointers to child nodes.

## Weaknesses
- **Limited interface**: Binary heaps only provide easy access to the smallest item. Finding other items in the heap takes O(n)O(n) time, since we have to iterate through all the nodes.


## Time Complexity 

Ops|Worst Case 
---|---|
Get min|O(1)
Remove min|O(lg(n))
Insert|O(lg(n))
Heapify|O(n)
Space|O(n)




# PriorityQueue



