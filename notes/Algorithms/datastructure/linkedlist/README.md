

# Linked Lists

## Defitions 
- Picture a linked list like a chain of paperclips linked together. It's quick to add another paperclip to the top or bottom. It's even quick to insert one in the middle—just disconnect the chain at the middle link, add the new paperclip, then reconnect the other half.
- An item in a linked list is called a node. The first node is called the head. The last node is called the tail.
- **Doubly linked list** has nodes that also reference the previous node.

> Doubly linked lists allow us to traverse our list backwards. In a singly linked list, if you just had a pointer to a node in the middle of a list, there would be no way to know what nodes came before it. Not a problem in a doubly linked list.

- **Circularly linked list** is simple linked list whose tail, the last node, references the head, the first node.


<p align="center">
  <img width="460" height="100" src="https://www.interviewcake.com/images/svgs/linked_list__nodes_and_pointers_labeled_head_and_tail.svg?bust=206">
</p>

> - Unlike an array, consecutive items in a linked list are not necessarily next to each other in memory.

## Strength 

- **Fast operations on the ends**: Adding elements at either end of a linked list is O(1)O(1). Removing the first element is also O(1)O(1).
- **Flexible size**: There's no need to specify how many elements you're going to store ahead of time. You can keep adding elements as long as there's enough space on the machine.

## Weaknesses

- **Costly lookups/access element**: To access or edit an item in a linked list, you have to take O(i) time to walk from the head of the list to the ith item.
- **Not cache-friendly**: Most computers have caching systems that make reading from sequential addresses in memory faster than reading from scattered addresses. **Array** items are always located right next to each other in computer memory, but linked list nodes can be scattered all over. So iterating through a linked list is usually quite a bit slower than iterating through the items in an array, even though they're both theoretically O(n) time.


## Uses

- Stacks and queues only need fast operations on the ends, so linked lists are ideal.

## Implementation: 
### Python 
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

### Java 
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

## Linked list v.s array 
### PROS
- **Dynamic size**: The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.

- **Ease of insertion/deletion** :Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted.

### CONS 
- **Random access is not allowed**: We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. 
- **Extra memory space for a pointer** is required with each element of the list.
- **Not cache friendly**: Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.

## Time Complexity

Ops|Worst Case 
---|---|
Space|O(n)
Prepend|O(1)
Append|O(1)
Lookup|O(n)
Insertion|O(n)
Deletion|O(n)