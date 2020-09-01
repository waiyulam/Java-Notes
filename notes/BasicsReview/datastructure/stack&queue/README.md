
# Queues

## Definitions 
- A queue stores items in a first-in, first-out (FIFO) order 
- Picture a queue like the line outside a busy restaurant. First come, first served.

<p align="center">
<img width='400' height = "150" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/02/Queue.png">
</p>

## Strengths

- **Fast operations**: All queue operations take O(1)O(1) time.

## Uses 
- **Breadth-first search** uses a queue to keep track of the nodes to visit next.
- **Printers** use queues to manage jobs—jobs get printed in the order they're submitted.
- **Web servers** use queues to manage requests—page requests get fulfilled in the order they're received.
- **Processes** wait in the CPU scheduler's queue for their turn to run.

## Implementation 
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

## Time Complexity

Ops|Worst Case 
---|---|
Space|O(n)
Enqueue|O(1)
Dequeue|O(1)
Peek|O(1)

# Stacks

## Definitions 
- A stack stores items in a last-in, first-out (LIFO) order.
- Picture a pile of dirty plates in your sink. As you add more plates, you bury the old ones further down. When you take a plate off the top to wash it, you're taking the last plate you put in. "Last in, first out."

<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/stack.png">
</p>


## Uses 

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


## Time Complexity 
Ops|Worst Case 
---|---|
Space|O(n)
Push|O(1)
Pull|O(1)
Peek|O(1)
