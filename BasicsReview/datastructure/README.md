
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
---------------------|----------------------------------------------------------------------|---------------------------------|---------------------------------|
[Static/Linear Array](#Static-Arrays)| <ul><li>Static array is a fixed length contatiner containing n elements **indexable** from the range [0,n-1] / 0 based index</li></ul>|<ul><li><b>Access</b>:O(1)</li><li><b>Search</b>:O(n) </li><li><b>Optiomal_Search</b>:O(log(n)) </li><li><b>Insertion</b>:N/A</li><li><b>Appending</b>:N/A</li><li><b>Deletion</b>:N/A</li> </ul>|  <ul><li>Bad at searching, inserting, and deleting</li><li>Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted</li></ul>
[Dynamic Array](#Dynamic-Arrays)| <ul><li>like one dimensional arrays but have **researved** space for additional elements</li><li> If a dynamic array is full, it **copies its contents to a larger array.**</li></ul>|<ul><li><b>Access</b>: O(1)</li><li><b>Search</b>: O(n) </li><li><b>Optiomal Search</b>:O(log(n)) </li><li><b>Insertion</b>: O(n) </li><li><b>Appending</b>: O(1)</li><li><b>Deletion</b>: O(n)</li></ul>| <ul><li>One limitation of arrays is that they're fixed size, A dynamic array expands as you add more elements. So you don't need to determine the size ahead of time.</li></ul>
[Linked List](#Linked-Lists)| <ul><li>linked list organizes items sequentially, with each item storing a pointer to the next one.</li><li>An item in a linked list is called a **node**. The first node is called the **head**. The last node is called the **tail**.|<ul><li><b>Access</b>: O(n)</li><li><b>Search</b>: O(n) </li><li><b>Insertion</b>: O(n)</li><li><b>Appending</b>: O(1) </li><li><b>Prepending</b>: O(1) </li><li><b>Deletion</b>: O(n)</li> </ul>| <ul><li>Ease of insertion/deletion compared to array</li><li>Adding elements at either end of a linked list is O(1). Removing the first element is also O(1)</li></ul>
[Queue](#Queue)|<ul><li>Stores items in a first-in first-out (FIFO) order</li>|<ul><li><b>Enqueue</b>: O(1)</li><li><b>Dequeue</b>: O(1) </li><li><b>Peek</b>: O(1)</li>|<ul><li>The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.</li></ul>
[Stack](#Stack)|<ul><li>Stores items in a last-in, first-out (LIFO) order</li></ul>|<ul><li><b>Push</b>: O(1)</li><li><b>Pop</b>: O(1) </li><li><b>Peek</b>: O(1)</li>|
[Hash table](hashtable)|<ul><li>Hash table provides a mapping from keys to values using a technique called **hashing**</li><li>Key-value pairs: key must be unique <li>Hash functions accept a key and return an output unique only to that specific key.</li><ul>|<ul><li><b>Insert</b>: O(1)/O(n)</li><li><b>Lookup</b>: O(1)/O(n) </li><li><b>Delete</b>: O(1)/O(n)</li></ul>|<ul><li>For arrays and linked lists, we need to search in a linear fashion, which can be costly in practice. If we use arrays and keep the data sorted, then a phone number can be searched in O(Logn) time using Binary Search, but insert and delete operations become costly as we have to maintain sorted order</li><li>Hashing  performs extremely well compared to above data structures like Array, Linked List in practice. With hashing we get O(1) search time on average (under reasonable assumptions) and O(n) in worst case.</li></ul>

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

### Implementation : Python 
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

### Implementation: 
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

## Queues 

### Definitions 
- A queue stores items in a first-in, first-out (FIFO) order 
- Picture a queue like the line outside a busy restaurant. First come, first served.

<p align="center">
<img width='400' height = "150" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png">
</p>

### Strengths

- **Fast operations**: All queue operations take O(1)O(1) time.

### Uses 
- **Breadth-first search** uses a queue to keep track of the nodes to visit next.
- **Printers** use queues to manage jobs—jobs get printed in the order they're submitted.
- **Web servers** use queues to manage requests—page requests get fulfilled in the order they're received.
- **Processes** wait in the CPU scheduler's queue for their turn to run.

### Implementation 
Queue can be implemented with a linked list/array. Made with a doubly linked list that only removes from head and adds to tail.
- To enqueue, insert at the tail of the linked list. If the queue is full, then it is said to be an Overflow condition.
- To dequeue, remove at the head of the linked list. If the queue is empty, then it is said to be an Underflow condition.

<details>
<summary><b>Java implementation</b></summary>

```java 
// Java program for linked-list implementation of queue 
  
// A linked list (LL) node to store a queue entry 
class QNode { 
    int key; 
    QNode next; 
  
    // constructor to create a new linked list node 
    public QNode(int key) 
    { 
        this.key = key; 
        this.next = null; 
    } 
} 
  
// A class to represent a queue 
// The queue, front stores the front node of LL and rear stores the 
// last node of LL 
class Queue { 
    QNode front, rear; 
  
    public Queue() 
    { 
        this.front = this.rear = null; 
    } 
  
    // Method to add an key to the queue. 
    void enqueue(int key) 
    { 
  
        // Create a new LL node 
        QNode temp = new QNode(key); 
  
        // If queue is empty, then new node is front and rear both 
        if (this.rear == null) { 
            this.front = this.rear = temp; 
            return; 
        } 
  
        // Add the new node at the end of queue and change rear 
        this.rear.next = temp; 
        this.rear = temp; 
    } 
  
    // Method to remove an key from queue. 
    void dequeue() 
    { 
        // If queue is empty, return NULL. 
        if (this.front == null) 
            return; 
  
        // Store previous front and move front one node ahead 
        QNode temp = this.front; 
        this.front = this.front.next; 
  
        // If front becomes NULL, then change rear also as NULL 
        if (this.front == null) 
            this.rear = null; 
    } 
} 
// Driver class 
public class Test { 
    public static void main(String[] args) 
    { 
        Queue q = new Queue(); 
        q.enqueue(10); 
        q.enqueue(20); 
        q.dequeue(); 
        q.dequeue(); 
        q.enqueue(30); 
        q.enqueue(40); 
        q.enqueue(50); 
        q.dequeue(); 
        System.out.println("Queue Front : " + q.front.key); 
        System.out.println("Queue Rear : " + q.rear.key); 
    } 
} 
```

</details>

<details>
<summary><b>Python implementation</b></summary>

```python 
# Python3 program to demonstrate linked list 
# based implementation of queue 
  
# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# A class to represent a queue 
  
# The queue, front stores the front node 
# of LL and rear stores the last node of LL 
class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def EnQueue(self, item): 
        temp = Node(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
  
# Driver Code 
if __name__== '__main__': 
    q = Queue() 
    q.EnQueue(10) 
    q.EnQueue(20) 
    q.DeQueue() 
    q.DeQueue() 
    q.EnQueue(30) 
    q.EnQueue(40) 
    q.EnQueue(50)  
q.DeQueue()    
    print("Queue Front " + str(q.front.data)) 
    print("Queue Rear " + str(q.rear.data)) 

```

</details>

> Notes: You could implement a queue with an array or dynamic array, but it would get kinda messy. Try drawing it out. You'll notice that you'd need to build out a "scoot over" or "re-center" operation that automatically fires when your queue items hit the bottom edge of the array.

### Time Complexity

Ops|Worst Case 
---|---|
Space|O(n)
Enqueue|O(1)
Dequeue|O(1)
Peek|O(1)

## Stacks

### Definitions 
- A stack stores items in a last-in, first-out (LIFO) order.
- Picture a pile of dirty plates in your sink. As you add more plates, you bury the old ones further down. When you take a plate off the top to wash it, you're taking the last plate you put in. "Last in, first out."

<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/stack.png">
</p>


### Uses 

- **The call stack** is a stack that tracks function calls in a program. When a function returns, which function do we "pop" back to? The last one that "pushed" a function call.
- **Depth-first search** uses a stack (sometimes the call stack) to keep track of which nodes to visit next.
- **String parsing—stacks** turn out to be useful for several types of string parsing.

### Implementation
Stack, commonly implemented with linked lists but can be made from arrays too. Made with a linked list by having the head be the only place for insertion and removal.
- **Push**: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
- **Pop**: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
- **Peek or Top**: Returns top element of stack.
- **isEmpty**: Returns true if stack is empty, else false.

<details>
<summary><b>Java implementation</b></summary>

```java 
// Java Code for Linked List Implementation 
  
public class StackAsLinkedList { 
  
    StackNode root; 
  
    static class StackNode { 
        int data; 
        StackNode next; 
  
        StackNode(int data) 
        { 
            this.data = data; 
        } 
    } 
  
    public boolean isEmpty() 
    { 
        if (root == null) { 
            return true; 
        } 
        else
            return false; 
    } 
  
    public void push(int data) 
    { 
        StackNode newNode = new StackNode(data); 
  
        if (root == null) { 
            root = newNode; 
        } 
        else { 
            StackNode temp = root; 
            root = newNode; 
            newNode.next = temp; 
        } 
        System.out.println(data + " pushed to stack"); 
    } 
  
    public int pop() 
    { 
        int popped = Integer.MIN_VALUE; 
        if (root == null) { 
            System.out.println("Stack is Empty"); 
        } 
        else { 
            popped = root.data; 
            root = root.next; 
        } 
        return popped; 
    } 
  
    public int peek() 
    { 
        if (root == null) { 
            System.out.println("Stack is empty"); 
            return Integer.MIN_VALUE; 
        } 
        else { 
            return root.data; 
        } 
    } 
  
    public static void main(String[] args) 
    { 
  
        StackAsLinkedList sll = new StackAsLinkedList(); 
  
        sll.push(10); 
        sll.push(20); 
        sll.push(30); 
  
        System.out.println(sll.pop() + " popped from stack"); 
  
        System.out.println("Top element is " + sll.peek()); 
    } 
} 
```

</details>

<details>
<summary><b>Python implementation</b></summary>

```python 
# Python program for linked list implementation of stack 
  
# Class to represent a node 
class StackNode: 
  
    # Constructor to initialize a node 
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class Stack: 
      
    # Constructor to initialize the root of linked list 
    def __init__(self): 
        self.root = None
  
    def isEmpty(self): 
        return True if self.root is None else  False 
  
    def push(self, data): 
        newNode = StackNode(data) 
        newNode.next = self.root  
        self.root = newNode 
        print "% d pushed to stack" %(data) 
      
    def pop(self): 
        if (self.isEmpty()): 
            return float("-inf") 
        temp = self.root  
        self.root = self.root.next 
        popped = temp.data 
        return popped 
      
    def peek(self): 
        if self.isEmpty(): 
            return float("-inf") 
        return self.root.data 
  
# Driver program to test above class  
stack = Stack() 
stack.push(10)         
stack.push(20) 
stack.push(30) 
  
print "% d popped from stack" %(stack.pop()) 
print "Top element is % d " %(stack.peek()) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
```

</details>


### Time Complexity 
Ops|Worst Case 
---|---|
Space|O(n)
Enqueue|O(1)
Dequeue|O(1)
Peek|O(1)


## Heap&PriorityQueue&Binary Heap
  -  [ ] [Intro](https://www.youtube.com/watch?v=t0Cq6tVNRBA&feature=youtu.be)


## Trees
-  [ ] [Intro](https://www.youtube.com/watch?v=oSWTXtMglKE&feature=youtu.be)
- Binary Tree
- Binary Search Tree
- AVL Tree (TODO)
- Suffix Tree (TODO)
- Segment Tree (TODO)

## Tries   
  -  [ ] [Intro](https://www.youtube.com/watch?v=zIjfhVPRZCg)

## Graphs   

## Others DS
  -  [ ] [Data Structure Intro](https://www.youtube.com/watch?v=bum_19loj9A)
  -  [ ] [Crash Course Computer Science](https://www.youtube.com/watch?v=DuDz6B4cqVc&feature=youtu.be)

