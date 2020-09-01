# B tree 
- [B Tree]()
    * [Definition](#Definition)
        - [Database Indexing](#Uses-Database-indexing)
    * [Operations](#Operations)
    * [Introduction of B+ Tree](#Introduction-of-B+-Tree)
    * [Difference between B tree and B+ tree](#Difference-between-B-tree-and-B+-tree)
    * [Difference between Binary tree and B-tree](#Difference-between-Binary-tree-and-B-tree)
    * [Time Complexity ](#Time-Complexity)

## Definition 

- All leaves are at the same level 

- A B-Tree is defined by the term minimum degree ‘t’. The value of t depends upon disk block size.

- Every node except root must contain **at least t-1 keys**. The root may contain minimum 1 key.

- All nodes (including root) may **contain at most 2t – 1 keys**.

- Number of children of a node is equal to the number of keys in it plus 1.

- All keys of a node are sorted in increasing order. The child between two keys k1 and k2 contains all keys in the range from k1 and k2.

- B-Tree grows and shrinks from the root which is unlike Binary Search Tree. Binary Search Trees grow downward and also shrink from downward.

- Like other balanced Binary Search Trees, time complexity to search, insert and delete is O(log n).

Following is an example of B-Tree of minimum order 5.

<p>
<img width = "500" height="200" src="https://media.geeksforgeeks.org/wp-content/uploads/20200506235136/output253.png">
</p>

> We can see in the above diagram that all the leaf nodes are at the same level and all non-leaf have no empty sub-tree and have keys one less than the number of their children.

### Uses Database indexing

- [Turotial](https://www.youtube.com/watch?v=aZjYr87r1b8)

B-Tree is a self-balancing search tree. In most of balancing binary search tree like AVL and Red black tree, B-Tree is assumed that everything in **Main memory/Disk**.  

- To understand the use of B Tree, we can think of B tree as following the multi-level indexing format.

The huge amount of data that cannot fit in main memory (single level indexing). When the number of keys is high, the data is read from disk in the form of blocks. **Disk access time is very high compared to the main memory access time.** 

- The main idea of using B-Trees is to **reduce the number of disk accesses.** 

-  B-tree is a fat tree. The height of B-Trees is kept low by **putting maximum possible keys in a B-Tree node** and all leaf node are at the same height(balanced).

Generally, the B-Tree node size is kept equal to the disk block size. Since the height of the B-tree is low so total disk accesses for most of the operations are reduced significantly compared to balanced Binary Search Trees like AVL Tree, Red-Black Tree, ..etc.

## Operations

### Search
Search is similar to the search in Binary Search Tree. Let the key to be searched be k. We start from the root and recursively traverse down. For every visited non-leaf node, if the node has the key, we simply return the node. Otherwise, we recur down to the appropriate child (The child which is just before the first greater key) of the node. If we reach a leaf node and don’t find k in the leaf node, we return NULL.

1. Search will start with root node 
2. Check in which range the key is i.e as key 120 is >100 and <130 so it has to be in left branch of the b tree 
<p align="center">
<img width = "400" height="200" src="https://media.geeksforgeeks.org/wp-content/uploads/20200507002619/output256.png">
</p>

### Insertion 

#### Split child 
Child y of x is being split into two nodes y and z. Note that the splitChild operation moves a key up and this is the reason B-Trees grow up, unlike BSTs which grow down.

<p align="center">
<img width = "400" height="200" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/BTreeSplit.jpg">
</p>

1) Initialize x as root.
2) While x is not leaf, do following
..a) Find the child of x that is going to be traversed next. Let the child be y.
..b) If y is not full, change x to point to y.
..c) If y is full, split it and change x to point to one of the two parts of y. If k is smaller than mid key in y, then set x as the first part of y. Else second part of y. When we split y, we move a key from y to its parent x.
3) The loop in step 2 stops when x is leaf. x must have space for 1 extra key as we have been splitting all nodes in advance. So simply insert k to x.

- The advantage of splitting before is, we never traverse a node twice. If we don’t split a node before going down to it and split it only if a new key is inserted (reactive), we may end up traversing all nodes again from leaf to root. This happens in cases when all nodes on the path from the root to leaf are full. So when we come to the leaf node, we split it and move a key up. Moving a key up will cause a split in parent node (because the parent was already full). This cascading effect never happens in this proactive insertion algorithm. There is a disadvantage of this proactive insertion though, we may do unnecessary splits.

#### Examples: 
minimum degree t as 3 and insrt a sequence of integers 10, 20, 30, 40, 50, 60, 70, 80 and 90

1) Initially root is NULL. Let us first insert 10.
<p align="center">
<img width = "300" height="100" src="https://www.geeksforgeeks.org/wp-content/uploads/Btree1.png">
</p>

2) Let us now insert 20, 30, 40 and 50. They all will be inserted in root because the maximum number of keys a node can accommodate is 2*t – 1 which is 5.
<p align="center">
<img width = "500" height="100" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/BTree2Ins.png">
</p>

3) Let us now insert 60. Since root node is full, it will first split into two, then 60 will be inserted into the appropriate child.
<p align="center">
<img width = "500" height="300" src="https://www.geeksforgeeks.org/wp-content/uploads/BTreeIns3.png">
</p>

4) Let us now insert 70 and 80. These new keys will be inserted into the appropriate leaf without any split.
<p align="center">
<img width = "500" height="200" src="https://www.geeksforgeeks.org/wp-content/uploads/BTreeIns4.png">
</p>

5) Let us now insert 90. This insertion will cause a split. The middle key will go up to the parent.
<p align="center">
<img width = "500" height="200" src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/BTreeIns6.png">
</p>

### Delete 

Deletion from a B-tree is more complicated than insertion, because we can delete a key from any node-not just a leaf—and when we delete a key from an internal node, we will have to rearrange the node’s children.

- Just as we had to ensure that a node didn’t get too big due to insertion, we must ensure that a node doesn’t get too small during deletion (except that the root is allowed to have fewer than the minimum number t-1 of keys). 

1. If the key k is in node x and x is a leaf, delete the key k from x.

2. If the key k is in node x and x is an internal node, do the following.

    - If the child y that precedes k in node x has at least t keys, then find the predecessor k0 of k in the sub-tree rooted at y. Recursively delete k0, and replace k by k0 in x. (We can find k0 and delete it in a single downward pass.)

    - If y has fewer than t keys, then, symmetrically, examine the child z that follows k in node x. If z has at least t keys, then find the successor k0 of k in the subtree rooted at z. Recursively delete k0, and replace k by k0 in x. (We can find k0 and delete it in a single downward pass.)

    - Otherwise, if both y and z have only t-1 keys, merge k and all of z into y, so that x loses both k and the pointer to z, and y now contains 2t-1 keys. Then free z and recursively delete k from y.

3. If the key k is not present in internal node x, determine the root x.c(i) of the appropriate subtree that must contain k, if k is in the tree at all. If x.c(i) has only t-1 keys, execute step 3a or 3b as necessary to guarantee that we descend to a node containing at least t keys. Then finish by recursing on the appropriate child of x.
    - If x.c(i) has only t-1 keys but has an immediate sibling with at least t keys, give x.c(i) an extra key by moving a key from x down into x.c(i), moving a key from x.c(i) ’s immediate left or right sibling up into x, and moving the appropriate child pointer from the sibling into x.c(i).

    - If x.c(i) and both of x.c(i)’s immediate siblings have t-1 keys, merge x.c(i) with one sibling, which involves moving a key from x down into the new merged node to become the median key for that node.

<p align="center">
<img width = "500" height="600" src="https://media.geeksforgeeks.org/wp-content/uploads/bplustree.png">
</p>

<p align="center">
<img width = "500" height="400" src="https://media.geeksforgeeks.org/wp-content/uploads/bplustr.png">
</p>

## Introduction of B+ Tree

### Structure of the internal nodes of a B+ tree

1. Each internal node is of the form :
< P1, K1, P2, K2, ….., Pc-1, Kc-1, Pc > 

> NOTE: In b tree, the node contain pairs of < k,data pointer >

where c <= a and each Pi is a tree pointer (i.e points to another node of the tree) and, each Ki is a key value (see diagram-I for reference).

2. Every internal node has : K1 < K2 < …. < Kc-1

3. For each search field values ‘X’ in the sub-tree pointed at by Pi, the following condition holds :
Ki-1 < X <= Ki, for 1 < i < c and,
Ki-1 < X, for i = c

4. Each internal nodes has at most ‘a’ tree pointers.

5. The root node has, at least two tree pointers, while the other internal nodes have at least \ceil(a/2) tree pointers each.

6. If any internal node has ‘c’ pointers, c <= a, then it has 'c – 1' key values.

<p align="center">
<img width = "400" height="200" src="https://media.geeksforgeeks.org/wp-content/uploads/diagram-I-1.jpg">
</p>


### The structure of the leaf nodes of a B+ tree of order ‘b’ is as follows:

1. Each leaf node is of the form :
<<K1, D1>, <K2, D2>, ….., <Kc-1, Dc-1>, Pnext>
where c <= b and each Di is a data pointer (i.e points to actual record in the disk whose key value is Ki or to a disk file block containing that record) and, each Ki is a key value and, Pnext points to next leaf node in the B+ tree (see diagram II for reference).
2. Every leaf node has : K1 < K2 < …. < Kc-1, c <= b
3. Each leaf node has at least \ceil(b/2) values.
4. All leaf nodes are at same level.

<p align="center">
<img width = "400" height="200" src="https://media.geeksforgeeks.org/wp-content/uploads/diagram-II.jpg">
</p>


### Linked leaf 

Using the Pnext pointer it is viable to traverse all the leaf nodes, just like a linked list, thereby achieving ordered access to the records stored in the disk.

<p align="center">
<img width = "400" height="200" src="https://media.geeksforgeeks.org/wp-content/uploads/Btree.jpg">
</p>

### Advantage

- A B+ tree with ‘l’ levels can **store more entries** in its internal nodes compared to a B-tree having the same ‘l’ levels. 

- This accentuates the **significant improvement made to the search time** for any given key. Having lesser levels and presence of Pnext pointers imply that B+ tree are **very quick and efficient in accessing records from disks**.

- 非叶子节点不会带上 ROWID，这样，一个块中可以容纳更多的索引项，一是可以降低树的高度。二是一个内部节点可以定位更多的叶子节点。

- 叶子节点之间通过指针来连接，范围扫描将十分简单，而对于B树来说，则需要在叶子节点和内部节点不停的往返移动。


## Difference between B tree and B+ tree

In order, to implement dynamic multilevel indexing, B-tree and B+ tree are generally employed. The drawback of B-tree used for indexing, however is that it stores the data pointer (a pointer to the disk file block containing the key value), corresponding to a particular key value, along with that key value in the node of a B-tree.

**This technique, greatly reduces the number of entries that can be packed into a node of a B-tree, thereby contributing to the increase in the number of levels in the B-tree, hence increasing the search time of a record**.

B+ tree eliminates the above drawback by storing data pointers only at the leaf nodes of the tree.  It may be noted here that, since data pointers are present only at the leaf nodes, the leaf nodes must necessarily store all the key values along with their corresponding data pointers to the disk file block, in order to access them. 
Moreover, the leaf nodes are linked to provide ordered access to the records. The leaf nodes, therefore form the first level of index, with the internal nodes forming the other levels of a multilevel index. Some of the key values of the leaf nodes also appear in the internal nodes, to simply act as a medium to control the searching of a record.

N.O|B-TREE|B+ TREE
-----|-------|-------|
1.|All internal and leaf nodes have data pointers	|Only leaf nodes have data pointers
2.|Since all keys are not available at leaf, search often takes more time.	|All keys are at leaf nodes, hence search is faster and accurate..
3.|No duplicate of keys is maintained in the tree.	|Duplicate of keys are maintained and all nodes are present at leaf.
4.|Insertion takes more time and it is not predictable sometimes.	|Insertion is easier and the results are always the same.
5.|Deletion of internal node is very complex and tree has to undergo lot of transformations.	|Deletion of any node is easy because all node are found at leaf.
6.|Leaf nodes are not stored as structural linked list.	|Leaf nodes are stored as structural linked list.
7.|对于在内部节点的数据，可直接得到，不必根据叶子节点来定位. No redundant search keys are present..|Redundant search keys may be present..

## Difference between Binary tree and B-tree

- Unlike binary tree, in B-tree, a node can have more than two children. B-tree has a height of logM N (Where ‘M’ is the order of tree and N is the number of nodes).

- The height is adjusts automatically at each update. In the B-tree data is sorted in a specific order, with the lowest value on the left and the highest value on the right.

There are some conditions that must be hold by the B-Tree:

- All the leaf nodes of the B-tree must be at the same level.
- Above the leaf nodes of the B-tree, there should be no empty sub-trees.
- B- tree’s height should lie as low as possible.

N.O|B-TREE|BINARY TREE
-----|-------|-------|
1.|In a B-tree, a node can have maximum ‘M'(‘M’ is the order of the tree) number of child nodes.|While in binary tree, a node can have maximum two child nodes or sub-trees.
2.|B-tree is called as sorted tree as its nodes are sorted in inorder traversal.|While binary tree is not a sorted tree. It can be sorted in inorder, preorder or postorder traversal.
3.|B-tree has a height of logM N (Where ‘M’ is the order of tree and N is the number of nodes).	|While binary tree has a height of log2 N(Where N is the number of nodes).
4.|B-Tree is performed when the data is loaded in the disk.	|Unlike B-tree, binary tree is performed when the data is loaded in the RAM(faster memory).
5.|B-tree is used in DBMS(code indexing, etc).	|While binary tree is used in Huffman coding and Code optimization and many others.
6.|To insert the data or key in B-tree is more complicated than binary tree.|While in binary tree, data insertion is not complicated than B-tree.


## Time Complexity 

Ops|Balanced|Worst case
-----|-----|------|
Space|O(n)|O(n)
Insert|O(log(n))|O(log(n))
Loopup|O(log(n))|O(log(n))
Delete|O(log(n))|O(log(n))

### Facts 
- The minimum height of the B-Tree that can exist with n number of nodes and m is the maximum number of children of a node can have is:

<p align="center">
<img width = "200" height="100" src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-b2583191e91c4ae6b918589495ad9302_l3.png">
</p>

- The maximum height of the B-Tree that can exist with n number of nodes and d is the minimum number of children that a non-root node can have is:

<p align="center">
<img width = "200" height="100" src="https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-91e6517dbf84093666399a4a6baf3bb6_l3.png">
</p>

