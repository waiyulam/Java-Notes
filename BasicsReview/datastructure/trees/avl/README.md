# AVL tree 
- [BBST](#Balanced-binary-search-tree)
    * [Tree Invariant ](#Tree-Invariant)
    * [Tree Rotation  ](#Tree-Rotation)

- [平衡二叉树 AVL Tree](#AVL-Tree)
    * [Definition](#Definition)
    * [AVL Invariant](#AVL-Tree-Invariant)
    * [Balancing operations](#Balancing-operations)
    * [Operations](#Operations)
    * [Comparison with Red Black Tree](#Comparison-with-Red-Black-Tree)
    * [Time Complexity ](#Time-Complexity)


# Balanced binary search tree

The secret ingredient to most balanced BST algorithms is the clever sage of a tree invariant and tree rotations 

## Tree Invariant 
- A property/rule you impose on tree that it must meet after every operation 

## Tree Rotation  
- To ensure that the invariant is alwas satisfied a series of tree rotations are normally applied 
<p align = "left">
<img width = "400" height="200" src="https://upload.wikimedia.org/wikipedia/commons/2/23/Tree_rotation.png">
</p>

In the left tree we know that A < P < B < Q < C and this remains true for the right subtree. So we didn't break the BST invariant and there fore this is a valid transformation

```python 
    def rightRotation(A):
        B = A.left 
        A.left = B.right 
        B.right = A 
        return B 

    def leftRotation(A):
        B = A.right
        A.right = B.left
        B.left = A 
        return B 
```

# [AVL Tree](https://www.growingwiththeweb.com/data-structures/avl-tree/overview/)

## Definition 
- AVL tree is a **self-balancing Binary Search Tree** (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.
- AVL tree allow for logarithmic insertion, deletion and search operations 

<p align = "left">
<img width = "300" height="200" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/AVL-Tree1.jpg">
<img width = "300" height="200" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/Not-AVL1.jpg">
</p>

The left tree is AVL because differences between heights of left and right subtrees for every node is less than or equal to 1. The right tree is not AVL because differences between heights of left and right subtrees for 8 and 12 is greater than 1.

## AVL Tree Invariant 

### Balanced Factor (BF) :  the property which keeps an AVL tree balanced 

<p align="center">
BF(node) = H(node.right) - H(node.left)
</p>

where H(x) is the height of node x which calculated as the **number of edges** between x and the furthest leaf 

- The invariant in the AVL which forces it to remain balanced is the requirement that the balanced factor is always either -1, 0 or +1 

### Node Information to store 

- The **actual value** we are storing in the node. NOTE: this value must be comparable so we know how to insert it 

- A value storing this node's **balance factor**

- The **height** of this node in the tree : The height of a node is defined as the maximum number of steps from the node to any of its leaf nodes. 

> h = max(h_left,h_right) + 1
> with the base case being a h = 0 for a leaf node.

- Pointers to the **left/right child nodes**

## Balancing operations

**Strategy to restore the AVL tree invariant** : When insertion or deletion occurs, the heights of nodes are updated and a balancing operation occurs. There are four different cases that can occur, each of them can be fixed using either one or two binary tree rotation operations.

> If a node's BF != {-1,0,1} then the BF of the node is +2 or -2 

### <li>Left left case</li>

This case occurs when the height of a **node’s left child becomes 2 greater than that of the right child**, and the left child is either **balanced or left-heavy**. It can be fixed using a single right rotate operation on the unbalanced node.

<p align = "center">
<img width = "300" height="150" src="https://www.growingwiththeweb.com/images/data-structures/avl-tree/balancing-left-left-case.svg">
</p>

### <li>Left right case</li>
This case occurs when the height of **a node’s left child becomes 2 greater than that of the right child**, and **the left child is right-heavy**. It can be fixed using a left rotate on the left child, which results in the left left case which is fixed using a right rotate on the unbalanced node.
<p align = "center">
<img width = "400" height="150" src="https://www.growingwiththeweb.com/images/data-structures/avl-tree/balancing-left-right-case.svg">
</p>

### <li>Right right case</li>
This case occurs when the height of a **node’s right child becomes 2 greater than that of the left child**, and the **right child is either balanced or right-heavy**. This is the inverse of the left left case. It can be fixed using a single left rotate operation on the unbalanced node.
<p align = "center">
<img width = "300" height="150" src="https://www.growingwiththeweb.com/images/data-structures/avl-tree/balancing-right-right-case.svg">
</p>

### <li>Right left case</li>
This case occurs when the **height of a node’s right child becomes 2 greater than that of the left child**, and **the right child is left-heavy**. This is the inverse of the left right case. It can be fixed using a right rotate on the right child, which results in the right right case which is fixed using a left rotate on the unbalanced node.
<p align = "center">
<img width = "400" height="150" src="https://www.growingwiththeweb.com/images/data-structures/avl-tree/balancing-right-left-case.svg">
</p>

### Implementation 

```python 
    def leftLeftCase(node):
        return rightRotation(node) 
    def leftRightCase(node):
        node.left = leftRotation(node.left)
        return leftLeftCase(node)
    def rightRightCase(node):
        return leftRotation(node)
    def rightLeftCase(node)：
        node.right = rightRotation(node.right)
        return rightRightCase(node)
``` 

> NOTE: After rotation update balance factor and height values i.e update(A) and update(B)
> AVL tree rotations require you to call the **update method**! 

<p align = "center">
<img width = "600" height="400" src="https://upload.wikimedia.org/wikipedia/commons/c/c4/Tree_Rebalancing.gif">
</p>

## Operations    

### Insertion 

Insert starts by performing a regular BST insert. Once the node is inserted, go up the tree updating the heights of each node and rebalancing when required as outlined in the balancing section.

```python 
    def update(node):
        # variables for left/right subtree heights 
        lh = -1
        rh = -1
        if node.left != None : lh = node.left.height
        if node.right != None : rh = node.right.height
        # Update node's height 
        node.height = 1+ max(lh,rh)
        # update balance factor 
        node.bf = rh - lh 

    def balance(node):
        # Left heavy subtree 
        if node.bf == -2:
            if node.left.bf <= 0:
                return leftLeftCase(node)
            else:
                return leftRightCase(node)
        # Right heavy subtree 
        else if node.bf == +2:
            if node.right.bf >= 0:
                return rightRightCase(node)
            else:
                return rightLeftCase(node)
        # Node has balance factor of -1,0 or +1
        # which we do not need to balance 
        return node 

    def insert(node,value):
        if node == None: return Node(value)
        cmp = compare(value,node.value)
        if cmp < 0:
            node.left = insert(node.left,value)
        else:
            node.right= insert(node.right,value)
        # Update balance factor and height values 
        update(node)

        # Rebalance tree 
        return balance(node)
```

### Delete 
Delete starts by performing a regular BST delete. Once the node is deleted, go up the tree updating the heights of each node and rebalancing when required as outlined in the balancing section.

1. Find the element we wish to remove (if it exists)
2. Replace the node we want to remove with its successor (if any) to maintain the BST invariant 
3. Starting from w, travel up and find the first unbalanced node.
4. Re-balance the tree by performing appropriate rotations on the subtree rooted with first unbalanced node. 

#### Case 1: Remove leaf node 
If the node we wish to remove is a leaf node then we may do so without any side effect

#### Case 2/Case 3: either the left/right child node is subtree 
The successor of the node we are trying to remove in these case will be **immediate node down from the left/right subtree**. 

#### Case 4: node to remove has both left and right subtree 
The successor can either be the largest value in the left subtree or the smallest value in the right subtree 

Once the successor node has been identified(if exists), replace the value of the node to remove with the value in the successor node. 

> NOTE: Don't forget to remove the duplicate value of the successor node that still exists in the tree -> calling the function again recursively but with the value to remove as the value in the successor node. 

### Search 
Search simply performs a BST search since the AVL maintains BST properties.

### [Source code](https://www.youtube.com/watch?v=tqFZzXkbbGY&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=51)

## Worst case balancing

The worst case balancing of the AVL tree occurs when one child on every node has a height of 1 more than the other child.

<p align = "center">
<img width = "600" height="400" src="https://www.growingwiththeweb.com/images/data-structures/avl-tree/worst-case-balancing.svg">
</p>
Notice how the example of a tree of height 3 is a node with the left child being the height 2 tree and right child being the height 1 tree. This illustrates the recurrence for the worst case height of a tree.

> F_h = F_(h-1) + F_(h-2) + 1

This recurrence is very similar to the Fibonacci sequence; Fortunately, just like the Fibonacci sequence, the number of nodes in a worst case balanced AVL tree increases exponentially. This means that the worst case height is still O(logn) even in a worst case balanced tree.

## Strengths 
The cost of these operations may become O(n) for a skewed Binary tree. If we make sure that height of the tree remains O(Logn) after every insertion and deletion, then we can guarantee an upper bound of O(Logn) for all these operations. The height of an AVL tree is always O(Logn) where n is the number of nodes in the tree 

## Comparison with Red Black Tree
The AVL tree and other self-balancing search trees like Red Black are useful to get all basic operations done in O(log n) time. The AVL trees are more balanced compared to Red-Black Trees, but they may cause more rotations during insertion and deletion. So if your application involves many frequent insertions and deletions, then Red Black trees should be preferred. And if the insertions and deletions are less frequent and search is the more frequent operation, then AVL tree should be preferred over Red Black Tree.

## Time Complexity 
The rotation operations (left and right rotate) take constant time as only a few pointers are being changed there. Updating the height and getting the balance factor also takes constant time. So the time complexity of AVL insert remains same as BST insert which is O(h) where h is the height of the tree. Since AVL tree is balanced, the height is O(Logn). So time complexity of AVL insert is O(Logn).

Ops|Balanced|Unbalanced(Worst case )
-----|-----|------|
Space|O(n)|O(n)
Insert|O(log(n))|O(log(n))
Loopup|O(log(n))|O(log(n))
Delete|O(log(n))|O(log(n))

## Which binary search tree is best?#
The AVL tree, red-black tree and splay tree are all self-adjusting binary search trees, so which one is better in which situation? And when is it better to use a regular BST?

A paper by Ben Pfaff of Stanford University performs an in-depth study of the performance characteristics of each tree under various circumstances. Each data structure excels based on runtime patterns in the input and the calling of operations. It comes to the following conclusions:

- Regular BSTs excel when randomly ordered input can be relied upon.
- Splay trees excel when data is often inserted in a sorted order and later accesses are sequential or clustered.
- AVL trees excel when data is often inserted in a sorted order and later accesses are random.
- Red-black trees excel when data is often inserted in random order but occasional runs of sorted order are expected.

