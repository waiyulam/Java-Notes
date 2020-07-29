
# Data Structures

<p align="center">
  <img width="460" height="300" src="https://res.cloudinary.com/practicaldev/image/fetch/s--WlnYH5fq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1600/1%2ADyu63sMUVL-gYEZISOE2BQ.jpeg">
</p>

- [Data Structures Easy to Advanced Course - Full Tutorial from a Google Engineer and ACM ICPC World Finalist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu)  

- [Commonly asked questions](https://www.geeksforgeeks.org/commonly-asked-data-structure-interview-questions-set-1/)

- [Interview tips: Data structure](https://yangshun.github.io/tech-interview-handbook/algorithms/array)

**NOTES**:

- If you are interested in how data structures are implemented, check out [Lago](https://github.com/yangshun/lago), a Data Structures and Algorithms library for JavaScript. 

- Data structures are your weapons. Choosing the right weapon for the right battle is the key to victory. Be very familiar about the strengths of each data structure and the time complexities for its various operations.

## Table of Contents 
- [Arrays](#Arrays)
- [Linked List](#Linked-Lists)
- [Stacks & Queues &Double-ended Queue](#Stacks-and-Queues)
- [Hash Tables](#Hash-Table)
- [Trees](#Trees)
- [Tries](#Tries)
- [Heaps&Priority Queue](#Heap&PriorityQueue&Binary-Heap)
- [Graphs](#Graphs)
- [Others](#Others-DS)

## Quick Reference 
DS | Def | Time Complexity | Others 
---|---|---|---|
[Static/Linear Array](#Static-Arrays)| <ul><li>Static array is a fixed length contatiner containing n elements **indexable** from the range [0,n-1] / 0 based index</li></ul>|<ul><li><b>Access</b>: O(1)</li><li><b>Search</b>: O(n) </li><li><b>Optiomal Search</b>: O(log(n)) </li><li><b>Insertion</b>: N/A</li><li><b>Appending</b>: N/A</li><li><b>Deletion</b>: N/A</li> </ul>|  <ul><li>Bad at searching, inserting, and deleting</li><li>Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted</li></ul>
[Dynamic Array](#Dynamic-Arrays)| <ul><li>like one dimensional arrays but have **researved** space for additional elements</li><li> If a dynamic array is full, it **copies its contents to a larger array.**</li></ul>|<ul><li><b>Access</b>: O(1)</li><li><b>Search</b>: O(n) </li><li><b>Optiomal Search</b>: O(log(n)) </li><li><b>Insertion</b>: O(n) </li><li><b>Appending</b>: O(1)</li><li><b>Deletion</b>: O(n)</li></ul>| <ul><li>One limitation of arrays is that they're fixed size, A dynamic array expands as you add more elements. So you don't need to determine the size ahead of time.</li></ul>
[Linked List](#Linked-Lists)| <ul><li>linked list organizes items sequentially, with each item storing a pointer to the next one.</li><li>An item in a linked list is called a **node**. The first node is called the **head**. The last node is called the **tail**.|<ul><li><b>Access</b>: O(n)</li><li><b>Search</b>: O(n) </li><li><b>Insertion</b>: O(n)</li><li><b>Appending</b>: O(1) </li><li><b>Prepending</b>: O(1) </li><li><b>Deletion</b>: O(n)</li> </ul>| <ul><li>Ease of insertion/deletion compared to array</li><li>Adding elements at either end of a linked list is O(1). Removing the first element is also O(1)</li></ul>




## [Static Arrays](https://www.interviewcake.com/concept/python/array?)

### Definition 
- A static array is a fixed length container containing n elements **indexable** from range [0,n-1]
- **Indexable**: each slot/index in the array can be referenced with a number 

### Uses
1. Storing and accessing sequential data 
2. Temporaritly storing objects 
3. Used by IO routines as buffers 
4. Lookup tables and inverse lookup tables 
5. Used as multiple values return or args input from a function 
6. Used in DP to cache ansers to subproblems 

### Strengths
- **Fast lookups**: Retrieving the element at a given index takes O(1) time, regardless of the length of the array.

### Weaknesses
- **Fixed size**: You need to specify how many elements you're going to store in your array ahead of time. (Unless you're using a fancy dynamic array.)
- **Costly inserts and deletes**: You have to "scoot over" the other elements to fill in or close gaps, which takes worst-case O(n) time.

### Declaration : java 
```java
 int gasPrices[] = new int[10];

gasPrices[0] = 346;
gasPrices[1] = 360;
gasPrices[2] = 354;
```

### Time Complexity 

Ops|Average Case|Worst Case 
---|---|---|
Space|O(n)|O(n)
Access|O(1)|O(1)
Appending|N/A|N/A
Insertion|N/A|N/A
Deletion|N/A|N/A

## [Dynamic Arrays](https://www.interviewcake.com/concept/python/dynamic-array)

### Definition 

- **Automatic Resizing**: like one dimensional arrays, but have **reserved space for additional elements**. If a dynamic array is full, it **copies its contents to a larger array.**

### Strengths

- **Fast lookups** :Just like arrays, retrieving the element at a given index takes O(1)O(1) time.
- **Variable size**: You can add as many items as you want, and the dynamic array will expand to hold them.
- **Cache-friendly**: Just like arrays, dynamic arrays place items right next to each other in memory, making efficient use of caches.

### Weaknesses

- **Slow worst-case appends**: Usually, adding a new element at the end of the dynamic array takes O(1)O(1) time. But if the dynamic array doesn't have any room for the new item, it'll need to expand(copy all the elements and double size of array), which takes O(n) time.
- **Costly inserts and deletes**: Just like arrays, elements are stored adjacent to each other. So adding or removing an item in the middle of the array requires "scooting over" other elements, which takes O(n) time.

### Declaration : Python 
```python 
# In Python, dynamic arrays are called lists.
gas_prices = []

gas_prices.append(346)
gas_prices.append(360)
gas_prices.append(354)
```

### Notes 

#### Size v.s Capacity 
![](https://www.interviewcake.com/images/svgs/dynamic_arrays__capacity_size_end_index.svg?bust=206)
We'd say this dynamic array's size is 4 and its capacity is 10. The dynamic array stores an end_index to keep track of where the dynamic array ends and the extra capacity begins.

#### Doubling Space 
What if we try to append an item but our array's capacity is already full?<br>
To make room, dynamic arrays automatically make a new, bigger underlying array. Usually twice as big. and each item has to be individually copied into the new array.

> Notes: Why not just extend the existing array? Because that memory might already be taken by another program.


### Time Complexity

Ops|Average Case|Worst Case 
---|---|---|
Space|O(n)|O(n)
Access|O(1)|O(1)
Appending|O(1)|O(n)
Insertion|O(n)|O(n)
Deletion|O(n)|O(n)

## Linked Lists

### Defitions 
- Picture a linked list like a chain of paperclips linked together. It's quick to add another paperclip to the top or bottom. It's even quick to insert one in the middle—just disconnect the chain at the middle link, add the new paperclip, then reconnect the other half.
- An item in a linked list is called a node. The first node is called the head. The last node is called the tail.
- **Doubly linked list** has nodes that also reference the previous node.

> Doubly linked lists allow us to traverse our list backwards. In a singly linked list, if you just had a pointer to a node in the middle of a list, there would be no way to know what nodes came before it. Not a problem in a doubly linked list.

- **Circularly linked list** is simple linked list whose tail, the last node, references the head, the first node.


<p align="center">
  <img width="460" height="100" src="https://www.interviewcake.com/images/svgs/linked_list__nodes_and_pointers_labeled_head_and_tail.svg?bust=206">
</p>

> - Unlike an array, consecutive items in a linked list are not necessarily next to each other in memory.

### Strength 

- **Fast operations on the ends**: Adding elements at either end of a linked list is O(1)O(1). Removing the first element is also O(1)O(1).
- **Flexible size**: There's no need to specify how many elements you're going to store ahead of time. You can keep adding elements as long as there's enough space on the machine.

### Weaknesses

- **Costly lookups/access element**: To access or edit an item in a linked list, you have to take O(i) time to walk from the head of the list to the ith item.
- **Not cache-friendly**: Most computers have caching systems that make reading from sequential addresses in memory faster than reading from scattered addresses. **Array** items are always located right next to each other in computer memory, but linked list nodes can be scattered all over. So iterating through a linked list is usually quite a bit slower than iterating through the items in an array, even though they're both theoretically O(n) time.


### Uses

- Stacks and queues only need fast operations on the ends, so linked lists are ideal.

### Declaration: 
#### Python 
```python 
# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize  
                          # next as null 
   
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
```

#### Java 
```java

class LinkedList { 
    Node head; // head of the list 
  
    /* Linked list Node*/
    class Node { 
        int data; 
        Node next; 
        // Constructor to create a new node 
        // Next is by default initialized 
        // as null 
        Node(int d) { data = d; } 
    } 
}
```

<details>
<summary><b>Traversals</b></summary>

```java 
// A simple Java program for traversal of a linked list 
class LinkedList { 
    Node head; // head of list 
  
    /* Linked list Node.  This inner class is made static so that 
       main() can access it */
    static class Node { 
        int data; 
        Node next; 
        Node(int d) 
        { 
            data = d; 
            next = null; 
        } // Constructor 
    } 
  
    /* This function prints contents of linked list starting from head */
    public void printList() 
    { 
        Node n = head; 
        while (n != null) { 
            System.out.print(n.data + " "); 
            n = n.next; 
        } 
    } 
  
    /* method to create a simple linked list with 3 nodes*/
    public static void main(String[] args) 
    { 
        /* Start with the empty list. */
        LinkedList llist = new LinkedList(); 
  
        llist.head = new Node(1); 
        Node second = new Node(2); 
        Node third = new Node(3); 
  
        llist.head.next = second; // Link first node with the second node 
        second.next = third; // Link first node with the second node 
  
        llist.printList(); 
    } 
}
```

</details>

### Linked list v.s array 
#### PROS
- **Dynamic size**: The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.

- **Ease of insertion/deletion** :Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted.

#### CONS 
- **Random access is not allowed**: We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. 
- **Extra memory space for a pointer** is required with each element of the list.
- **Not cache friendly**: Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.

### Time Complexity

Ops|Worst Case 
---|---|
Space|O(n)
Prepend|O(1)
Append|O(1)
Lookup|O(n)
Insertion|O(n)
Deletion|O(n)

## Stacks and Queues

Stack, commonly implemented with linked lists but can be made from arrays too.
Stacks are last in, first out (LIFO) data structures.
Made with a linked list by having the head be the only place for insertion and removal.

Queues, too can be implemented with a linked list or an array.
Queues are a first in, first out (FIFO) data structure.
Made with a doubly linked list that only removes from head and adds to tail.



## Hash Table   
  -  [ ] [Intro](https://www.youtube.com/watch?v=shs0KM3wKv8&feature=youtu.be)
  -  [ ] [Phone Book Problem](https://www.coursera.org/learn/data-structures/lecture/NYZZP/phone-book-problem)


## Trees
-  [ ] [Intro](https://www.youtube.com/watch?v=oSWTXtMglKE&feature=youtu.be)
- Binary Tree
- Binary Search Tree
- AVL Tree (TODO)
- Suffix Tree (TODO)
- Segment Tree (TODO)

## Tries   
  -  [ ] [Intro](https://www.youtube.com/watch?v=zIjfhVPRZCg)

## Heap&PriorityQueue&Binary Heap
  -  [ ] [Intro](https://www.youtube.com/watch?v=t0Cq6tVNRBA&feature=youtu.be)

## Graphs   

## Others DS
  -  [ ] [Data Structure Intro](https://www.youtube.com/watch?v=bum_19loj9A)
  -  [ ] [Crash Course Computer Science](https://www.youtube.com/watch?v=DuDz6B4cqVc&feature=youtu.be)

