# Binary Search Tree 

- [Definition](#Definition)
- [Balanced Binary Search Trees](#Balanced-Binary-Search-Trees)
- [Implementation](#Implementation)]
- [Strengths](#Strengths)
- [Weaknesses](#Weaknesses)
- [Hash table v.s BST](#Hash-table-v.s-BST)
- [Time Complexity](#Time-Complexity)

## Definition 

A binary search tree is a binary tree where the nodes are ordered in a specific way. For every node:

- The nodes to the left are smaller than the current node.

- The nodes to the right are larger than the current node.

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/bst__binary_search_tree.svg?bust=206">
</p>

## Balanced Binary Search Trees

<p align="center">
<img width="400" height="300" src="https://www.interviewcake.com/images/svgs/bst__balanced_non_balanced.svg?bust=206">
</p>

> Some trees (like AVL trees or Red-Black trees) rearrange nodes as they're inserted to ensure the tree is always balanced. With these, the worst case complexity for searching, inserting, or deleting is always O(lg(n)), not O(n).

## Strengths

- **Good performance across the board**. Assuming they're balanced, binary search trees are good at lots of operations, even if they're not constant time for anything.

    * Compared to a sorted array, lookups take the same amount of time ( O(lg(n))), but inserts and deletes are faster (O(lg(n)) for BSTs, O(n) for arrays).

    * Compared to hash table, BSTs have better worst case performance—O(lg(n)) instead of O(n). But, on average dictionaries perform better than BSTs (meaning O(1) time complexity).

- **BSTs are sorted**. Taking a binary search tree and pulling out all of the elements in sorted order can be done in O(n) using an in-order traversal. Finding the element closest to a value can be done in O(lg(n)) (again, if the BST is balanced!).

## Implementation 

### Note Look up

1. Start from root.
2. Compare the inserting element with root, if less than root, then recurse for left, else recurse for right.
3. If element to search is found anywhere, return true, else return false.

### Node Insertion 

A new key is always inserted at leaf. We start searching a key from root till we hit a leaf node. Once a leaf node is found, the new node is added as a child of the leaf node.

1. Start from root.
2. Compare the inserting element with root, if less than root, then recurse for left, else recurse for right.
3. After reaching end,just insert that node at left(if less than current) else right.

### Node Removal

- **Node to be deleted is leaf**: Simply remove from the tree.
- **Node to be deleted has only one child**: Copy the child to the node and delete the child
- **Node to be deleted has two children**: Find inorder successor of the node. Copy contents of the inorder successor to the node and delete the inorder successor. (i.e inorder successor can be obtained by finding the minimum value in right child of the node.)

<details>
<summary><b>Java Source code</b></summary>

```java
// Java program to demonstrate delete operation in binary search tree 
class BinarySearchTree 
{ 
    /* Class containing left and right child of current node and key value*/
    class Node 
    { 
        int key; 
        Node left, right; 
  
        public Node(int item) 
        { 
            key = item; 
            left = right = null; 
        } 
    } 
  
    // Root of BST 
    Node root; 
  
    // Constructor 
    BinarySearchTree() 
    { 
        root = null; 
    } 
  
    // This method mainly calls deleteRec() 
    void deleteKey(int key) 
    { 
        root = deleteRec(root, key); 
    } 
  
    /* A recursive function to insert a new key in BST */
    Node deleteRec(Node root, int key) 
    { 
        /* Base Case: If the tree is empty */
        if (root == null)  return root; 
  
        /* Otherwise, recur down the tree */
        if (key < root.key) 
            root.left = deleteRec(root.left, key); 
        else if (key > root.key) 
            root.right = deleteRec(root.right, key); 
  
        // if key is same as root's key, then This is the node 
        // to be deleted 
        else
        { 
            // node with only one child or no child 
            if (root.left == null) 
                return root.right; 
            else if (root.right == null) 
                return root.left; 
  
            // node with two children: Get the inorder successor (smallest 
            // in the right subtree) 
            root.key = minValue(root.right); 
  
            // Delete the inorder successor 
            root.right = deleteRec(root.right, root.key); 
        } 
  
        return root; 
    } 
  
    int minValue(Node root) 
    { 
        int minv = root.key; 
        while (root.left != null) 
        { 
            minv = root.left.key; 
            root = root.left; 
        } 
        return minv; 
    } 
  
    // This method mainly calls insertRec() 
    void insert(int key) 
    { 
        root = insertRec(root, key); 
    } 
  
    /* A recursive function to insert a new key in BST */
    Node insertRec(Node root, int key) 
    { 
  
        /* If the tree is empty, return a new node */
        if (root == null) 
        { 
            root = new Node(key); 
            return root; 
        } 
  
        /* Otherwise, recur down the tree */
        if (key < root.key) 
            root.left = insertRec(root.left, key); 
        else if (key > root.key) 
            root.right = insertRec(root.right, key); 
  
        /* return the (unchanged) node pointer */
        return root; 
    } 
  
    // This method mainly calls InorderRec() 
    void inorder() 
    { 
        inorderRec(root); 
    } 
  
    // A utility function to do inorder traversal of BST 
    void inorderRec(Node root) 
    { 
        if (root != null) 
        { 
            inorderRec(root.left); 
            System.out.print(root.key + " "); 
            inorderRec(root.right); 
        } 
    } 
  
    // Driver Program to test above functions 
    public static void main(String[] args) 
    { 
        BinarySearchTree tree = new BinarySearchTree(); 
  
        /* Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
        20   40  60   80 */
        tree.insert(50); 
        tree.insert(30); 
        tree.insert(20); 
        tree.insert(40); 
        tree.insert(70); 
        tree.insert(60); 
        tree.insert(80); 
  
        System.out.println("Inorder traversal of the given tree"); 
        tree.inorder(); 
  
        System.out.println("\nDelete 20"); 
        tree.deleteKey(20); 
        System.out.println("Inorder traversal of the modified tree"); 
        tree.inorder(); 
  
        System.out.println("\nDelete 30"); 
        tree.deleteKey(30); 
        System.out.println("Inorder traversal of the modified tree"); 
        tree.inorder(); 
  
        System.out.println("\nDelete 50"); 
        tree.deleteKey(50); 
        System.out.println("Inorder traversal of the modified tree"); 
        tree.inorder(); 
    } 
} 
```

</details>

- 
## Weaknesses:

- **Poor performance if unbalanced**: Some types of binary search trees balance automatically, but not all. If a BST is not balanced, then operations become O(n).

- **No O(1) operation** BSTs aren't the fastest for anything. On average, a list or a dictionary will be faster.

## Hash table v.s BST

Hash Table supports following operations in Θ(1) time.
1) Search
2) Insert
3) Delete

The time complexity of above operations in a self-balancing Binary Search Tree (BST) (like Red-Black Tree, AVL Tree, Splay Tree, etc) is O(Logn).

So Hash Table seems to beating BST in all common operations. When should we prefer BST over Hash Tables, what are advantages. Following are some important points in favor of BSTs.

1. We can get all keys in **sorted order** by just doing Inorder Traversal of BST. This is not a natural operation in Hash Tables and requires extra efforts.

2. Doin **finding closest lower and greater elements, doing range queries** are easy to do with BSTs. Like sorting, these operations are not a natural operation with Hash Tables.

3. With Self-Balancing BSTs, all operations are guaranteed to work in O(Logn) time. But with Hashing, Θ(1) is average time and some particular operations may be costly, especially **when table resizing happens**.

## Time Complexity 

Ops|Balanced|Unbalanced(Worst case )
-----|-----|------|
Space|O(n)|O(n)
Insert|O(log(n))|O(n)
Loopup|O(log(n))|O(n)
Delete|O(log(n))|O(n)



