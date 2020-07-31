# Data Structures

<p align="center">
  <img width="460" height="300" src="https://res.cloudinary.com/practicaldev/image/fetch/s--WlnYH5fq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1600/1%2ADyu63sMUVL-gYEZISOE2BQ.jpeg">
</p>

- [Data Structures Easy to Advanced Course - Full Tutorial from a Google Engineer and ACM ICPC World Finalist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu)  

- [Data Structures Reference for coding interviews](https://www.interviewcake.com/data-structures-reference)

- [Commonly asked questions](https://www.geeksforgeeks.org/commonly-asked-data-structure-interview-questions-set-1/)

- [Interview tips: Data structure](https://yangshun.github.io/tech-interview-handbook/algorithms/array)

**NOTES**:

- If you are interested in how data structures are implemented, check out [Lago](https://github.com/yangshun/lago), a Data Structures and Algorithms library for JavaScript. 

- Data structures are your weapons. Choosing the right weapon for the right battle is the key to victory. Be very familiar about the strengths of each data structure and the time complexities for its various operations.

## Quick Reference 

### Linear data strucutres 

#### <li>[表/数组 Arrays](array)</li>
DS | Def | Time Complexity | Others 
---------------------|----------------------------------------------------------------------|---------------------------------|---------------------------------|
[Static/Linear Array](array#Static-Arrays)| <ul><li>Static array is a fixed length contatiner containing n elements **indexable** from the range [0,n-1] / 0 based index</li></ul>|<ul><li><b>Access</b>:O(1)</li><li><b>Search</b>:O(n) </li><li><b>Optiomal_Search</b>:O(log(n)) </li><li><b>Insertion</b>:N/A</li><li><b>Appending</b>:N/A</li><li><b>Deletion</b>:N/A</li> </ul>|  <ul><li>Bad at searching, inserting, and deleting</li><li>Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted</li></ul>
[Dynamic Array](array#Dynamic-Arrays)| <ul><li>like one dimensional arrays but have **researved** space for additional elements</li><li> If a dynamic array is full, it **copies its contents to a larger array.**</li></ul>|<ul><li><b>Access</b>: O(1)</li><li><b>Search</b>: O(n) </li><li><b>Optiomal Search</b>:O(log(n)) </li><li><b>Insertion</b>: O(n) </li><li><b>Appending</b>: O(1)</li><li><b>Deletion</b>: O(n)</li></ul>| <ul><li>One limitation of arrays is that they're fixed size, A dynamic array expands as you add more elements. So you don't need to determine the size ahead of time.</li></ul>

#### <li>[链式结构 Linked List](linkedlist)</li>
DS | Def | Time Complexity | Others 
---------------------|----------------------------------------------------------------------|---------------------------------|---------------------------------|
[Linked_List](linkedlist)| <ul><li>linked list organizes items sequentially, with each item storing a pointer to the next one.</li><li>An item in a linked list is called a **node**. The first node is called the **head**. The last node is called the **tail**.|<ul><li><b>Access</b>:O(n)</li><li><b>Search</b>:O(n) </li><li><b>Insertion</b>: O(n)</li><li><b>Appending</b>:O(1) </li><li><b>Prepending</b>:O(1) </li><li><b>Deletion</b>: O(n)</li> </ul>| <ul><li>Ease of insertion/deletion compared to array</li><li>Adding elements at either end of a linked list is O(1). Removing the first element is also O(1)</li></ul>
[Queue](stack&queue#Queues)|<ul><li>Stores items in a first-in first-out (FIFO) order</li>|<ul><li><b>Enqueue</b>: O(1)</li><li><b>Dequeue</b>: O(1) </li><li><b>Peek</b>: O(1)</li>|<ul><li>The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.</li></ul>
[Stack](stack&queue#Stacks)|<ul><li>Stores items in a last-in, first-out (LIFO) order</li></ul>|<ul><li><b>Push</b>: O(1)</li><li><b>Pop</b>: O(1) </li><li><b>Peek</b>: O(1)</li>|

#### <li>[哈希表 Hash table](hashtable)</li>
DS | Def | Time Complexity | Others 
---------------------|----------------------------------------------------------------------|---------------------------------|---------------------------------|
[Hash_table](hashtable)|<ul><p><li>Hash table provides a mapping from keys to values using a technique called **hashing**</li></p><li>Key-value pairs: key must be unique <li>Hash functions accept a key and return an output unique only to that specific key.</li><ul>|<ul><li><b>Insert</b>:O(1)/O(n)</li><li><b>Lookup</b>:O(1)/O(n) </li><li><b>Delete</b>:O(1)/O(n)</li></ul>|<ul><li>For arrays and linked lists, we need to search in a linear fashion, which can be costly in practice. If we use arrays and keep the data sorted, then a phone number can be searched in O(Logn) time using Binary Search, but insert and delete operations become costly as we have to maintain sorted order</li><li>Hashing  performs extremely well compared to above data structures like Array, Linked List in practice. With hashing we get O(1) search time on average (under reasonable assumptions) and O(n) in worst case.</li></ul>

#### <li>[堆 Heaps](heap)</li>
DS | Def | Time Complexity | Others 
---------------------|----------------------------------------------------------------------|---------------------------------|---------------------------------|
[Binary_Heap](heap#Binary-Heap)|<ul><li>A binary heap is a **binary tree** where the **smallest/largest value** is always at the **top**</li><li>Heaps are implemented as **complete binary trees**.</li><li>Heaps are built on lists</li></ul>|<ul><li><b>Get min/max</b>: O(1)</li><li><b>Remove min</b>: O(1og(n))</li><li><b>Insert</b>: O(1og(n))</li><li><b>Heapify</b>:O(n)</li><li><b>Random_access</b>:O(n)</li>|<ul><li>Quickly access the smallest item</li><li>Binary heaps are usually implemented with **lists**, saving the overhead cost of storing pointers to child nodes.</li><li>Binary heaps only provide easy access to the smallest item. Finding other items in the heap takes O(n) time</li>
[Priority_Queue](heap#PriorityQueue)|<ul><li>Every item in the queue has a priority</li><li>Higher-priority items are dequeued before lower-priority items.</li>|<ul><li><b>Enqueue</b>: O(lg(n))</li><li><b>Dequeue</b>: O(lg(n)) </li><li><b>Peek</b>: O(1)</li>|<ul><li>Priority queues allow you to peek at the top item in O(1) while keeping other operations relatively cheap (O(lg(n)).</li></ul>



### Non-linear data strucutres 

#### <li>[Tree](trees)</li>

DS | Def | Time Complexity | Others 
-----|-------|--------|--------|
[Binary Search Tree](trees/binary)|<ul><li>A binary search tree is a binary tree where the nodes are ordered in a specific way.</li><li>The nodes to the left are smaller than the current node.</li><li>The nodes to the right are larger than the current node.</li>|<ul><li><b>Insert</b>:O(lg(n))/O(n)</li><li><b>Lookup</b>:O(lg(n))/O(n) </li><li><b>Delete</b>:O(lg(n))/O(n)</li>|<ul><li>Compared to a sorted array, lookups take the same amount of time ( O(lg(n))), but inserts and deletes are faster (O(lg(n)) for BSTs, O(n) for arrays).</li><li>Poor performance if unbalanced</li><li>BSTs aren't the fastest for anything. On average, a list or a dictionary will be faster.</li></ul>
[AVL tree](trees/avl)|<ul><li>AVL tree is a **self-balancing Binary Search Tree** (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.</li><li>AVL tree allow for logarithmic insertion, deletion and search operations </li>|<ul><li><b>Insert</b>:O(lg(n))</li><li><b>Lookup</b>:O(lg(n)) </li><li><b>Delete</b>:O(lg(n))</li></ul>|<ul><li>The invariant in the AVL which forces it to remain balanced is the requirement that the balanced factor is always either -1, 0 or +1 </li><li>The AVL trees are more balanced compared to Red-Black Trees, but they may cause more rotations during insertion and deletion.</li></ul>
[Red Black Tree](trees/rb)|<ul><li>Every node has a **color either red or black**</li><li> Root property : **Root of tree is always black**</li><li>Red property: There are no two adjacent red nodes **(A red node cannot have a red parent or red child).**</li><li>Depth property: Every path from a node (including root) to any of its **descendant NULL node** has **the same number of black nodes**.</li><li>External property: Every leaf (NULL) is counted as black.</li>|<ul><li><b>Insert</b>:O(lg(n))</li><li><b>Lookup</b>:O(lg(n)) </li><li><b>Delete</b>:O(lg(n))</li></ul>|<ul><li>B tree are more balanced than Red Black Tree (i.e the height of RB tree > the height of B tree normally)</li></ul>



- B Tree (TODO)
- Suffix Tree (TODO)
- Segment Tree (TODO)



## Tries   
  -  [ ] [Intro](https://www.youtube.com/watch?v=zIjfhVPRZCg)

## Graphs   

## Others DS
  -  [ ] [Data Structure Intro](https://www.youtube.com/watch?v=bum_19loj9A)
  -  [ ] [Crash Course Computer Science](https://www.youtube.com/watch?v=DuDz6B4cqVc&feature=youtu.be)

