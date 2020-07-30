# Binary Heap & Priority Queue 

- [Binary Heap](#Binary-Heap)
  + [Definition](#Heap-Definition)
    * [Types](#Types)
    * [Uses](#Heap-Uses)
  + [Implementation](#Implementation)
    * [Complete Trees](#Heaps-are-implemented-as-complete-binary-trees)
    * [Heaps are built on lists](#Heaps-are-built-on-lists)
    * [Insertion](#Insertion-:-O(log(n)))
    * [Removal](#Removing-the-smallest-item-:-O(log(n)))
  + [Heapify](#Heapify)
  + [Strengths](#Strengths)
  + [Weaknesses](#Weaknesses)
  + [Time complexity](#Time-Complexity)


- [Priority Queue](#PriorityQueue)

# Binary Heap

## Heap Definition

- A binary heap is a **binary tree** where the **smallest value** is always at the **top**

<p align="center">
<img weight="300" height="200" src="https://www.geeksforgeeks.org/wp-content/uploads/MinHeapAndMaxHeap.png">
</p>

### Types 

- **Max Heap**: the key present at the root node must be greatest among the keys presented at all of its children. **The same property must be recursively true for all sub trees in that Binary Tree**

- **Min Heap**: the key present at the root node must be minimum among the keys presented at all of its children. **The same property must be recursively true for all sub trees in that Binary Tree**

### Heap Uses

- **Priority queues**: implemented using heaps. Items are enqueued by adding them to the heap, and the highest-priority item can quickly be grabbed from the top.
- **Heap sort**: make a heap out of them and then remove items one at a time—in sorted order.

## Implementation 

### Heaps are implemented as complete binary trees

> In a complete binary tree:
> - Each level is filled up before another level is added
> - The bottom tier is filled in **from left to right**.  
> As we'll see, this allows us to efficiently store our heap as a list.

### Heaps are built on lists

- Complete trees and heaps are often stored as lists, one node after the other, like this:
<p align="center">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap_concept_page_diagrams__complete_trees.svg?bust=206">
</p>

- Using a list to store a complete binary tree is very efficient because there no need to spend extra space for pointer. Since there are no gaps in complete tree (Each level is filled up before another level is added and bottom tier is filled in **from left to right**. ), there are no unused bucket/slots in the list/array. 

- Inserting a new item in the bottom right part of the tree just means appending to the list.

#### **How do we traverse the tree when it's a list?**
With a bit of clever indexing

- **Left Child**: Index 0's left child is at index 1. Index 1's left child is at index 3. And index 2's left child is a 5. In general, a node at index ii's left child will be at index **2*i + 1**

- **Right Child**: This node always comes right after the left child. In general, a node at index ii's right child will be at index **2*i + 2**

- **Parent**: The nodes at indices 1 and 2 have their parent at index 0. The nodes at indices 3 and 4 have their parent at index 1. And the nodes at indices 5 and 6 have their parent at index 2. In general, a node at index i has its parent at index **(i-1)/2**

>Just remember the main idea is that you're multiplying or dividing by 2. This makes sense, because the number of nodes on each level of a complete binary tree doubles as you move down level by level.

### In a heap, **every node is smaller than its children**.
<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap__binary_tree_with_comparing_node_1_and_lower_level.svg?bust=206">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap__binary_tree_with_comparing_node_5_and_lower_level.svg?bust=206">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap__binary_tree_with_comparing_node_2_and_lower_level.svg?bust=206">
</p>

### Insertion : O(log(n))

1. Add the item to the bottom of the tree 
<p align="center">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap_concept_page_diagrams__implementation_overview__2_2a.svg?bust=206">
</p>

2. Compare the item with its parent. If the new item is smaller, swap the two.
<p align="center">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap_concept_page_diagrams__implementation_overview__2_2b.svg?bust=206">
</p>

3. Continue comparing and swapping, allowing the new item to **"bubble up"** until the it's larger than its parent.
<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap_concept_page_diagrams__implementation_overview__2_3b.svg?bust=206">
</p>

- Because our heap is built on a complete binary tree, we know it's also **balanced**. Which means the height of the tree is log(n). So we'll do at most log(n) of these swaps, giving us a total time cost of O(log(n)).

### Removing the smallest item : O(log(n))

1. Remove the root 
<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap_concept_page_diagrams__implementation_overview__2_a.svg?bust=206">
</p>

2. Take the bottom level's right-most item and move it to the top, to fill in the hole.
<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap_concept_page_diagrams__implementation_overview__1_1.svg?bust=206">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap_concept_page_diagrams__implementation_overview__1_2b.svg?bust=206">
</p>

3. Compare the item with its children: 

If it's larger than **either** child, swap the item with the smaller of the two children.
<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap_concept_page_diagrams__implementation_overview__1_4a.svg?bust=206">
</p>

4. Continue comparing and swapping, allowing the item to **"bubble down"** until it's smaller than its children.
<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap_concept_page_diagrams__implementation_overview__1_4b.svg?bust=206">
</p>

- As with inserting (above), we'll do at most log(n) of these swaps, giving us a total time cost of O(log(n))

### Source Code 

<details>
<summary><b>Python</b></summary>

```python 
# A Python program to demonstrate common binary heap operations 
  
# Import the heap functions from python library 
from heapq import heappush, heappop, heapify  
  
# heappop - pop and return the smallest element from heap 
# heappush - push the value item onto the heap, maintaining 
#             heap invarient 
# heapify - transform list into heap, in place, in linear time 
  
# A class for Min Heap 
class MinHeap: 
      
    # Constructor to initialize a heap 
    def __init__(self): 
        self.heap = []  
  
    def parent(self, i): 
        return (i-1)/2
      
    # Inserts a new key 'k' 
    def insertKey(self, k): 
        heappush(self.heap, k)            
  
    # Decrease value of key at index 'i' to new_val 
    # It is assumed that new_val is smaller than heap[i] 
    def decreaseKey(self, i, new_val): 
        self.heap[i]  = new_val  
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
            # Swap heap[i] with heap[parent(i)] 
            self.heap[i] , self.heap[self.parent(i)] = ( 
            self.heap[self.parent(i)], self.heap[i]) 
              
    # Method to remove minium element from min heap 
    def extractMin(self): 
        return heappop(self.heap) 
  
    # This functon deletes key at index i. It first reduces 
    # value to minus infinite and then calls extractMin() 
    def deleteKey(self, i): 
        self.decreaseKey(i, float("-inf")) 
        self.extractMin() 
  
    # Get the minimum element from the heap 
    def getMin(self): 
        return self.heap[0] 
  
# Driver pgoratm to test above function 
heapObj = MinHeap() 
heapObj.insertKey(3) 
heapObj.insertKey(2) 
heapObj.deleteKey(1) 
heapObj.insertKey(15) 
heapObj.insertKey(5) 
heapObj.insertKey(4) 
heapObj.insertKey(45) 
  
print heapObj.extractMin(), 
print heapObj.getMin(), 
heapObj.decreaseKey(2, 1) 
print heapObj.getMin() 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
```

</details>

## Heapify

**Transform a List Into a Heap** 

- We could create a new empty heap and add in the items from the list one at a time. If the list has n elements, then this takes **O(n*log(n))**

### Implementation : Bubbling down 

- More efficient: We'll take our input list and treat it like the nodes in a complete binary tree, just like we did above:

<p align="center">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heapsort__input_list_as_binary_tree.svg?bust=206">
</p>

To transform the tree into a valid heap, we'll compare each node to its children and move nodes around so that parent nodes are always smaller than their children.This causes larger nodes to move lower in the tree, **"bubbling down"** to allow smaller values to reach the top.

> Look familiar? This is the same bubbling down we were doing to remove items from the heap!

1) We'll work from the leaf-nodes at the bottom upwards. To start off, let's look at the leaves. The leaf nodes don't have any children, so they don't need to move down at all. Great.

<p align="center">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heapsort__binary_tree_with_highlighted_bottom_level.svg?bust=206">
</p>

2) Let's look at the nodes in the next level:

<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heapsort__binary_tree_with_highlighted_two_levels.svg?bust=206">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heapsort__binary_subtree_nodes_3_7_9.svg?bust=206">
</p>

Since 3 is smaller than both 7 and 9, it's already in the right spot.

But, looking at the right node (2) and its children, since 1 is smaller than 2, we'll swap them.

<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap__binary_tree_with_swapped_nodes_1_and_2.svg?bust=206">
</p>

3) Moving up, we've got an 8 at the root.

Since 8 is larger than 1, 8 bubbles down, swapping places with the smaller child: 1.

<p align="left">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap__binary_tree_with_swapped_nodes_8_and_1.svg?bust=206">
<img weight="300" height="200" src="https://www.interviewcake.com/images/svgs/heap__binary_tree_with_swapped_nodes_8_and_2.svg?bust=206">
</p>


At this point, we've transformed the input tree into a valid min heap. Nice!

### [Heapify complexity: O(n)](https://www.interviewcake.com/concept/python/heap)

- It's tempting to say it's O(n*log(n)). After all, we have to examine all n nodes, and a node might bubble down O(log(n)) levels.

That's an overestimate of the amount of work though. All of the leaf nodes at the bottom of the tree won't have to move down at all. And the parents of those nodes will only move down once. In fact, there's only one node that might move down O(log(n)) times: the root node.

- After computing the time complexity carefully, we finally get the O(n)

## Strengths
- **Quickly access the smallest item**: Binary heaps allow you to grab the smallest item (the root) in O(1) time, while keeping other operations relatively cheap (O(lg(n)) time).
- **Space efficient**: Binary heaps are usually implemented with **lists**, saving the overhead cost of storing pointers to child nodes.

## Weaknesses
- **Limited interface**: Binary heaps only provide easy access to the smallest item. Finding other items in the heap takes O(n) time, since we have to iterate through all the nodes.


## Time Complexity

Ops|Worst Case 
---|---|
Get min|O(1)
Remove min|O(lg(n))
Insert|O(lg(n))
Heapify|O(n)
Space|O(n)




# PriorityQueue



