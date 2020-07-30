# Tree

- [Definition](#Definition)
    + [Leaves, Depth, and Height](#Leaves-Depth-and-Height)
- [Tree Traversals](#Tree-Traversals)
    + [Breadth First Search(BFS)](#Breadth-First-Search)
    + [Depth First Search(DFS)](#Depth-First-Search)
    + [Pre Order Traversal](#Pre-Order-Traversal)
    + [In Order Traversal](#In-Order-Traversal)
    + [Post Order Traversal](#Post-Order-Traversal)
- [Binary Trees](#Binary-Trees)
- [Uses](#Uses)


## Definition 

- A tree organizes values hierarchically.

<p align="center">
<img width="500" height="200" src="https://www.interviewcake.com/images/svgs/trees__animal_classes.svg?bust=206">
</p>

- Each entry in the tree is called a **node**, and every node links to zero or more child nodes.

### Leaves Depth and Height

- **Leaf** : nodes that're on the bottom of the tree (more formally: nodes that have no children).

- **Depth**: Each node in a tree has a depth: the number of links from the root to the node.

- **Height**: A tree's height is the number of links from its root to the furthest leaf. (That's the same as the maximum node depth.)


<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__depth_height.svg?bust=206">
</p>

## Tree Traversals

### Breadth First Search

In a BFS, you first explore all the nodes one step away, then all the nodes two steps away, etc..

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__bfs.svg?bust=206">
</p>

### Depth First Search

In a DFS, you go as deep as possible down one path before backing up and trying a different one.

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__dfs.svg?bust=206">
</p>

> - Depth-first search on a binary tree generally requires less memory than breadth-first.

> - Depth-first search can be easily implemented with recursion.

> - A BFS will find the shortest path between the starting point and any other reachable node. A depth-first search will not necessarily find the shortest path.

### Pre Order Traversal

Visit the current node, then walk the left subtree, and finally walk the right subtree.

> A pre-order traversal usually visits nodes in the same order as a DFS.

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__pre_order_traversal.svg?bust=206">
</p>

### In Order Traversal

Walk the left subtree first, then visit the current node, and finally walk the right subtree.

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__in_order_traversal.svg?bust=206">
</p>

> Of all three traversal methods, this one is probably the most common. When walking a binary search tree, an in order traversal visits the nodes in sorted, ascending order.

### Post Order Traversal

Walk the left subtree, then the right subtree, and finally visit the current node.

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__post_order_traversal.svg?bust=206">
</p>

> This one's kind of rare ... but it shows up in some parsing algorithms, like Reverse Polish Notation.


## Binary Trees

A binary tree is a tree where every node has at most two children.

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__binary_non_binary.svg?bust=206">
</p>

- **Full binary trees** : a binary tree where every node has exactly **0 or 2 children**.

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__full_binary.svg?bust=206">
</p>

- **Perfect binary trees** : A perfect binary tree doesn't have room for any more nodes—unless we increase the tree's height.

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__perfect_binary.svg?bust=206">
</p>

- **Complete binary trees**: a perfect binary tree missing a few nodes in the last level. Nodes are filled in from left to right

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/trees__complete_binary.svg?bust=206">
</p>

> Complete trees are the basis for heaps and priority queues.

- **Balanced binary trees**:  a tree whose height is small relative to the number of nodes it has. By small, we usually mean the height is O(lg(n)), where n is the number of nodes.

Conceptually, a balanced tree "looks full," without any missing chunks or branches that end much earlier than other branches.

> There are few different definitions of balanced depending on the context. One of the most common definition is that a tree is balanced if: (a) the heights of its left and right subtrees differ by at most 1, and (b) both subtrees are also balanced.

<p align="center">
<img width="600" height="300" src="https://www.interviewcake.com/images/svgs/trees__balanced_unbalanced_binary.svg?bust=206">
</p>

## Relationship between height and number of nodes

In perfect binary trees there's a cool mathematical relationship between the number of nodes and the height of the tree.

1. Level 0: 2^0 =1 nodes,
2. Level 1: 2^1 =2 nodes,
3. Level 2: 2^2 =4 nodes,
4. Level 3: 2^3 =8nodes,

Let's call the total number of nodes in the tree n, and the height of the tree h.

- We could solve for n by adding up the number of nodes on each level in the tree:

<p align="center">

- n = 2^0 + 2^1 + 2^2 +..... = 2^h - 1
- h = log_2(n+1)

</p>

This is the intuition behind our definition of balanced that we used above. A perfect tree is balanced, and in a perfect tree the height grows logarithmically with the number of nodes.

## Uses 

- **Filesystems—files** inside folders inside folders
- **Comments—comments** replies to comments, replies to replies
- **Family trees—parents** grandparents, children, and grandchildren

