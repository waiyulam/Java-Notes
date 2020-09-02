# Red Black Tree 
- [Red Black Tree]()
    * [Definition](#Definition)
    * [Red Black Invariant](#Red-Black-Invariant)
    * [Balancing operations](#Balancing-operations)
    * [Operations](#Operations)
    * [Comparison with Red Black Tree](#Comparison-with-Red-Black-Tree)
    * [Time Complexity ](#Time-Complexity)

## Definition 

A red-black tree is a binary search tree with one extra attribute for each node: the colour, which is either red or black. We also need to keep track of the parent of each node, so that a red-black tree's node structure would be:

``` java
    class t_red_black_node {
        enum colour = { red, black }
        void *item;
        t_red_black_node.left = t_red_black_node()
        t_red_black_node.right = t_red_black_node()
        t_red_black_node.parent = t_red_black_node()
    }
```

<p align="center">
<img width="300" height="100" src="https://www.cs.auckland.ac.nz/software/AlgAnim/fig/rb_tree1a.gif">
</p>

### Why RBT ?
If we make sure that height of the tree remains O(Logn) after every insertion and deletion, then we can guarantee an upper bound of O(Logn) for all these operations. The height of a Red-Black tree is always O(Logn) where n is the number of nodes in the tree.

 
## Red Black Invariant

1. Every node has a **color either red or black**

2. Root property : **Root of tree is always black**

3. Red property: There are no two adjacent red nodes **(A red node cannot have a red parent or red child).**
> This property implys that any path from a node can't have #red nodes > #black nodes

4. Depth property: Every path from a node (including root) to any of its **descendant NULL node** has **the same number of black nodes**.

5. External property: Every leaf (NULL) is counted as black.


```
A chain of 3 nodes is nodes is not possible in Red-Black Trees. 
Following are NOT Red-Black Trees
        B              B                 B       
       / \            /  \             /  \
     B  NIL          R   NIL          R   NIL
    / \             / \              /  \   
   B  NIL           B  NIL          R  NIL  
Violates          Violates        Violates
Property 4.      Property 4       Property 3 

Following are different possible Red-Black Trees with above 3 keys
         B                            B
       /   \                        /   \
      B      B                    R      R
    /  \   /  \                 /  \    /  \
 NIL  NIL NIL NIL             NIL  NIL NIL NIL
 ``` 

### Black height 

The number of black nodes on any path from, but not including, a node x to a leaf is called the black-height of a node, denoted bh(x). 

We can prove the following lemma:

1. From above properties 3 and 4, we can derive, a Red-Black Tree of height h has **black-height >= h/2**. 

> Number of nodes from a node to its farthest descendant leaf is no more than twice as the number of nodes to the nearest descendant leaf.

2. Every Red Black Tree with n nodes has height <= 2Log2(n+1)

> This demonstrates why the red-black tree is a good search tree: it can always be searched in O(log n) time.

<details>
<summary><b>PROOF</b></summary>

1. For a general Binary Tree, let k be the minimum number of nodes on all root to NULL paths, then n >= 2k – 1 (Ex. If k is 3, then n is atleast 7). This expression can also be written as k <= Log2(n+1)

2. From property 4 of Red-Black trees and above claim, we can say in a Red-Black Tree with n nodes, there is a root to leaf path with at-most Log2(n+1) black nodes.

3. From property 3 of Red-Black trees, we can claim that the number black nodes in a Red-Black tree is at least ⌊ n/2 ⌋ where n is the total number of nodes.

From above 2 points, we can conclude the fact that Red Black Tree with n nodes has height <= 2Log2(n+1)

</details>

## Balancing operations
Recap: In AVL tree insertion, we used **rotation** as a tool to do balancing after insertion caused imbalance. In Red-Black tree, we use two tools to do balancing (if node's parent is red and violate property 3/property 4).

1. Rotation 
2. Recolring 

We try recoloring first, if recoloring doesn’t work, then we go for rotation. Following is detailed algorithm. The algorithms has mainly two cases depending upon the color of uncle. If uncle is red, we do recoloring. If uncle is black, we do rotations and/or recoloring.

> Color of a NULL node is considered as BLACK.

### If x’s uncle is RED (Grand parent must have been black from property 4)

1. Change color of parent and uncle as Black 
2. Color of grand parent as RED 
3. Change x = x's grandparent, repeat steps 2 and 3 for new x 

<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/redBlackCase2.png">
</p>

### If x’s uncle is BLACK

There can be four configurations for x, x’s parent (p) and x’s grandparent (g) (This is similar to AVL Tree)

#### Left Left Case (p is left child of g and x is left child of p)

1. Right Rotate g 
2. Swap colors of g and p ( g is red and p is black)

<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/redBlackCase3a1.png">
</p>

#### Left Right Case (p is left child of g and x is right child of p)

1. Left Rotate p 
2. Apply left left case above 

<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/redBlackCase3b.png">
</p>

#### Right Right Case (Mirror of case i)

1. Left rotate g 
2. Swap colors of g and p 

<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/redBlackCase3c.png">
</p>

#### Right Left Case (Mirror of case ii)

1. Right Rotate p 
2. Apply right right case above 

<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/redBlackCase3d.png">
</p>

## Operations

### Insertions 
Let x be the newly inserted node.

1) Perform standard BST insertion and make the color of newly inserted nodes **as RED**.

2) **If x is root, change color of x as BLACK** (Black height of complete tree increases by 1).

3) Double red: **Do the balancing operations if color of x’s parent is not BLACK and x is not root**.

<p align="center">
<img width="300" height="200" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/Examples_new.png">
</p>

> [source code](https://www.geeksforgeeks.org/c-program-red-black-tree-insertion/)

### [Delete](https://www.youtube.com/watch?v=_c30ot0Kcis)

In insert operation, we check color of uncle to decide the appropriate case. In delete operation, we **check color of sibling to decide the appropriate case**.

**The main property that violates after insertion is two consecutive reds**. In delete, the main violated property is, **change of black height in subtrees as deletion of a black node** may cause reduced black height in one root to leaf path.

When a black node is deleted and replaced by a black child, the child is marked as double black. The main task now becomes to convert this double black to single black.

1. Perform standard BST delete. When we perform standard delete operation in BST, we always end up deleting a node which is either leaf or has only one child (For an internal node, we copy the successor and then recursively call delete for successor, successor is always a leaf node or a node with one child).So we only need to handle cases where a node is leaf or has one child. Let v be the node to be deleted and u be the child that replaces v (Note that u is NULL when v is a leaf and color of NULL is considered as Black).

2. Simple Case: If either u or v is red, we mark the replaced child as black (No change in black height). Note that both u and v cannot be red as v is parent of u and two consecutive reds are not allowed in red-black tree.

<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/rbdelete11.png">
</p>

3. **Double black : If Both u and v are Black.**

a)  Color u as double black.  Now our task reduces to convert this double black to single black.

> Note that If v is leaf, then u is NULL and color of NULL is considered as black. So the deletion of a black leaf also causes a double black.

b) Do following while the current node u is double black and it is not root. Let sibling of node be s. 


<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/rbdelete12_new.png">
</p>

i.  **If sibling s is black and at least one of sibling’s children is red**
    
perform rotation(s). Let the red child of s be r. This case can be divided in four subcases depending upon positions of s and r.

(i) Left Left Case (s is left child of its parent and r is left child of s or both children of s are red). This is mirror of right right case shown in below diagram.

(ii) Left Right Case (s is left child of its parent and r is right child). This is mirror of right left case shown in below diagram.

(iii) Right Right Case (s is right child of its parent and r is right child of s or both children of s are red)

<p align="center">
<img width="300" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/rbdelete13New.png">
</p>

(iv) Right Left Case (s is right child of its parent and r is left child of s)

<p align="center">
<img width="300" height="200" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/rbdelete14.png">
</p>

ii.  **If sibling is black and its both children are black**

perform recoloring, and recur for the parent if parent is black

<p align="center">
<img width="300" height="200" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/rbdelete15.png">
</p>

In this case, if parent was red, then we didn’t need to recur for prent, we can simply make it black (red + double black = single black)

iii. **If sibling is red**

perform a rotation to move old sibling up, recolor the old sibling and parent. The new sibling is always black (See the below diagram). This mainly converts the tree to black sibling case (by rotation) and  leads to case (a) or (b). This case can be divided in two subcases.

(i) Left Case (s is left child of its parent). This is mirror of right right case shown in below diagram. We right rotate the parent p.

(iii) Right Case (s is right child of its parent). We left rotate the parent p.

<p align="center">
<img width="300" height="200" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/rbdelete161.png">
</p>

c) If u is root, make it single black and return (Black height of complete tree reduces by 1).

> [Source code](https://www.geeksforgeeks.org/red-black-tree-set-3-delete-2/)


## Comparison with B Tree

- B tree are more balanced than Red Black Tree (i.e the height of RB tree > the height of B tree normally)

- B+ Tree stores data at all leaf nodes and use linked list to connect them

## Time Complexity 

Ops|Balanced|Unbalanced(Worst case )
-----|-----|------|
Space|O(n)|O(n)
Insert|O(log(n))|O(log(n))
Loopup|O(log(n))|O(log(n))
Delete|O(log(n))|O(log(n))