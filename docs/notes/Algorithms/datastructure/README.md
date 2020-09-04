<p align="center">
  <img width="460" height="300" src="https://res.cloudinary.com/practicaldev/image/fetch/s--WlnYH5fq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1600/1%2ADyu63sMUVL-gYEZISOE2BQ.jpeg">
</p>


> 数据结构是您的`武器`。选择正确的武器进行正确的战斗是`胜利的关键`。学习目标是能够说出每种数据结构的优势以及各种操作的时间复杂性以及能够熟练利用数据结构来协助解决问题。

> 本文摘自：[Labuladong 的 fucking-algorithm](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%AD%A6%E4%B9%A0%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%92%8C%E7%AE%97%E6%B3%95%E7%9A%84%E9%AB%98%E6%95%88%E6%96%B9%E6%B3%95.md)

## 一、数据结构的存储方式

<font color="deepPink">数据结构的存储方式只有两种：数组（顺序存储）和链表（链式存储）。</font>

这句话怎么理解，不是还有散列表、栈、队列、堆、树、图等等各种数据结构吗？

我们分析问题，一定要有递归的思想，自顶向下，从抽象到具体。你上来就列出这么多，那些都属于「上层建筑」，而**数组和链表才是「结构基础」**。因为那些多样化的数据结构，究其源头，都是在链表或者数组上的特殊操作，API 不同而已。比如说:

`「队列」、「栈」`这两种数据结构既可以使用链表也可以使用数组实现。用`数组`实现，**就要处理扩容缩容的问题**；用`链表`实现，没有这个问题，**但需要更多的内存空间存储节点指针**。 

`「图」`的两种表示方法，邻接表就是链表，邻接矩阵就是二维数组。邻接矩阵判断连通性迅速，并可以进行矩阵运算解决一些问题，但是如果图比较稀疏的话很耗费空间。邻接表比较节省空间，但是很多操作的效率上肯定比不过邻接矩阵。

`「散列表」`就是通过散列函数把键映射到一个大数组里。而且对于解决散列冲突的方法，拉链法需要链表特性，操作简单，但需要额外的空间存储指针；线性探查法就需要数组特性，以便连续寻址，不需要指针的存储空间，但操作稍微复杂些。

`「树」`，用数组实现就是`「堆」`，因为「堆」是一个完全二叉树，用数组存储不需要节点指针，操作也比较简单；用链表实现就是很常见的那种「树」，因为不一定是完全二叉树，所以不适合用数组存储。为此，在这种链表「树」结构之上，又衍生出各种巧妙的设计，比如二叉搜索树、AVL 树、红黑树、区间树、B 树等等，以应对不同的问题。

了解 Redis 数据库的朋友可能也知道，Redis 提供列表、字符串、集合等等几种常用数据结构，但是对于每种数据结构，底层的存储方式都至少有两种，以便于根据存储数据的实际情况使用合适的存储方式。

综上，数据结构种类很多，甚至你也可以发明自己的数据结构，但是底层存储无非数组或者链表，**二者的优缺点如下**：

- `数组`: 
  * 由于是**紧凑连续存储**,可以**随机访问**，通过索引快速找到对应元素;
  * 而且相对**节约存储空间**。但正因为**连续存储，内存空间必须一次性分配够**，所以说数组如果要**扩容**，需要重新分配一块更大的空间，再把数据全部复制过去，**时间复杂度 O(N)**;
  * 而且你如果想在**数组中间进行插入和删除**，每次**必须搬移后面的所有数据**以保持连续，**时间复杂度 O(N)**;

- `链表`: 
  * 因为元素不连续，而是靠指针指向下一个元素的位置，所以**不存在数组的扩容问题**;
  * 如果知道**某一元素的前驱和后驱**，操作指针即可**删除该元素或者插入新元素，时间复杂度 O(1)**;
  * 但是正因为**存储空间不连续**，你无法根据一个索引算出对应元素的地址，所以**不能随机访问**;
  * 而且由于每个元素必须**存储指向前后元素位置的指针**，会**消耗相对更多的储存空间**。


## 二、数据结构的基本操作
对于任何数据结构，其基本操作**无非遍历 + 访问**，再具体一点就是：`增删查改`。

数据结构种类很多，但它们存在的目的都是在<font color="deepPink">不同的应用场景，尽可能高效地增删查改</font>。话说这不就是数据结构的使命么？

如何遍历 + 访问？我们仍然从最高层来看，各种数据结构的遍历 + 访问无非两种形式：`线性的和非线性的`。线性就是**for/while 迭代为代表**，非线性就是**递归为代表**。再具体一步，无非以下几种框架：

1. 数组遍历框架，典型的线性迭代结构：

```java
void traverse(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        // 迭代访问 arr[i]
    }
}
```

2. 链表遍历框架，兼具迭代和递归结构：

```java
/* 基本的单链表节点 */
class ListNode {
    int val;
    ListNode next;
}

void traverse(ListNode head) {
    for (ListNode p = head; p != null; p = p.next) {
        // 迭代访问 p.val
    }
}

void traverse(ListNode head) {
    // 递归访问 head.val
    traverse(head.next)
}
```

3. 二叉树遍历框架，典型的非线性递归遍历结构: 

```java
/* 基本的二叉树节点 */
class TreeNode {
    int val;
    TreeNode left, right;
}

void traverse(TreeNode root) {
    traverse(root.left)
    traverse(root.right)
}
```

```java
/* 二叉树框架可以扩展为 N 叉树的遍历框架 */
/* 基本的 N 叉树节点 */
class TreeNode {
    int val;
    TreeNode[] children;
}

void traverse(TreeNode root) {
    for (TreeNode child : root.children)
        traverse(child)
}
```

你看二叉树的递归遍历方式和链表的递归遍历方式，相似不？再看看二叉树结构和单链表结构，相似不？如果再多几条叉，N 叉树你会不会遍历？N 叉树的遍历又可以扩展为图的遍历，因为图就是好几 N 叉棵树的结合体。你说图是可能出现环的？这个很好办，用个**布尔数组 visited 做标记就行了**，这里就不写代码了。

所谓框架，就是套路。不管增删查改，这些代码都是永远无法脱离的结构，你可以把这个结构作为大纲，根据具体问题在框架上添加代码就行了，下面会具体举例。

## 三、学习指南

### 1. 这是啥？

这个问题最容易解决，就像一层窗户纸，你只要随便找本书看两天，自己动手实现一个「队列」「栈」之类的数据结构，就能捅破这层窗户纸。

这时候你就能理解「框架思维」文章中的前半部分了：<font color="deepPink">数据结构无非就是数组、链表为骨架的一些特定操作而已；每个数据结构实现的功能无非<b>增删查改</b>罢了</font>。

比如说「列队」这个数据结构，无非就是基于数组或者链表，实现 enqueue 和 dequeue 两个方法。这两个方法就是增和删呀，连查和改的方法都不需要。

### 2. 有啥用？

解决这个问题，就涉及算法的设计了，是个持久战，需要经常进行抽象思考，刷算法题，培养「计算机思维」。

之前的文章讲了，算法就是对数据结构准确而巧妙的运用。常用算法问题也就那几大类，算法题无非就是不断变换场景，给那几个算法框架套上不同的皮。刷题，就是在锻炼你的眼力，看你能不能看穿问题表象揪出相应的解法框架。

比如说，让你求解一个迷宫，你要把这个问题层层抽象：<font color="RoyalBlue">迷宫 -> 图的遍历 -> N 叉树的遍历 -> 二叉树的遍历。然后让框架指导你写具体的解法</font>。

**抽象问题，直击本质**，是刷题中你需要刻意培养的能力。

### 3. 如何看书

直接推荐一本公认的好书，《算法第 4 版》，我一般简写成《算法4》。不要蜻蜓点水，这本书你能选择性的看上 50%，基本上就达到平均水平了。别怕这本书厚，因为起码有三分之一不用看，下面讲讲怎么看这本书。

看书仍然遵循递归的思想：自顶向下，逐步求精。

这本书知识结构合理，讲解也清楚，所以可以按顺序学习。**书中正文的算法代码一定要亲自敲一遍**，因为这些真的是扎实的基础，要认真理解。不要以为自己看一遍就看懂了，不动手的话理解不了的。但是，开头部分的基础可以酌情跳过；书中的数学证明，如不影响对算法本身的理解，完全可以跳过；章节最后的练习题，也可以全部跳过。这样一来，这本书就薄了很多。

相信读者现在已经认可了「框架性思维」的重要性，这种看书方式也是<font color="deepPink">一种框架性策略，抓大放小，着重理解整体的<b>知识架构</b>，而忽略证明、练习题这种<b>细节问题</b>，即保持自己对新知识的好奇心，避免陷入无限的细节被劝退。</font>

当然，《算法4》到后面的内容也比较难了，比如那几个著名的串算法，以及正则表达式算法。这些属于「经典算法」，看个人接受能力吧，单说刷 LeetCode 的话，基本用不上，量力而行即可。

## 四、框架思维

<font color="deepPink">先刷二叉树，先刷二叉树，先刷二叉树！</font>

大部分人对数据结构相关的算法文章不感兴趣，而是更关心动规回溯分治等等技巧。为什么要先刷二叉树呢，因为**二叉树是最容易培养框架思维的，而且大部分算法技巧，本质上都是树的遍历问题**。

刷二叉树看到题目没思路？根据很多读者的问题，其实大家不是没思路，只是没有理解我们说的`「框架」`是什么。不要小看这几行破代码，几乎所有二叉树的题目都是一套这个框架就出来了。

```java
void traverse(TreeNode root) {
    // 前序遍历 pre-order ： 根结点 ---> 左子树 ---> 右子树
    traverse(root.left)
    // 中序遍历 In-Order ：左子树---> 根结点 ---> 右子树
    traverse(root.right)
    // 后序遍历 Post-Order ： 左子树 ---> 右子树 ---> 根结点
}
```
比如说我随便拿几道题的解法出来，不用管具体的代码逻辑，只要看看框架在其中是如何发挥作用的就行。

`后序遍历`: LeetCode 124 题，难度 Hard，让你求二叉树中最大路径和，主要代码如下：
```java
int ans = INT_MIN;
int oneSideMax(TreeNode* root) {
    if (root == nullptr) return 0;
    int left = max(0, oneSideMax(root->left));
    int right = max(0, oneSideMax(root->right));
    ans = max(ans, left + right + root->val);
    return max(left, right) + root->val;
}
```

`前序遍历`: LeetCode 105 题，难度 Medium，让你根据前序遍历和中序遍历的结果还原一棵二叉树，很经典的问题吧，主要代码如下：

```java
TreeNode buildTree(int[] preorder, int preStart, int preEnd, 
    int[] inorder, int inStart, int inEnd, Map<Integer, Integer> inMap) {

    if(preStart > preEnd || inStart > inEnd) return null;

    TreeNode root = new TreeNode(preorder[preStart]);
    int inRoot = inMap.get(root.val);
    int numsLeft = inRoot - inStart;

    root.left = buildTree(preorder, preStart + 1, preStart + numsLeft, 
                          inorder, inStart, inRoot - 1, inMap);
    root.right = buildTree(preorder, preStart + numsLeft + 1, preEnd, 
                          inorder, inRoot + 1, inEnd, inMap);
    return root;
}
```
不要看这个函数的参数很多，只是为了控制数组索引而已，本质上该算法也就是一个前序遍历。

`中序遍历`: LeetCode 99 题，难度 Hard，恢复一棵 BST，主要代码如下：
```java
void traverse(TreeNode* node) {
    if (!node) return;
    traverse(node->left);
    if (node->val < prev->val) {
        s = (s == NULL) ? prev : s;
        t = node;
    }
    prev = node;
    traverse(node->right);
}
```
这不就是个中序遍历嘛，对于一棵 BST 中序遍历意味着什么，应该不需要解释了吧。你看，Hard 难度的题目不过如此，而且还这么有规律可循，只要把框架写出来，然后往相应的位置加东西就行了，这不就是思路吗。

对于一个理解二叉树的人来说，刷一道二叉树的题目花不了多长时间。那么如果你对刷题无从下手或者有畏惧心理，不妨从二叉树下手，前 10 道也许有点难受；结合框架再做 20 道，也许你就有点自己的理解了；刷完整个专题，再去做什么回溯动规分治专题，你就会发现**只要涉及递归的问题，都是树的问题。**

动态规划详解说过凑零钱问题，暴力解法就是遍历一棵 N 叉树：

```python
def coinChange(coins: List[int], amount: int):

    def dp(n):
        if n == 0: return 0
        if n < 0: return -1

        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)
        return res if res != float('INF') else -1
    
    return dp(amount)
```

这么多代码看不懂咋办？直接提取出框架，就能看出核心思路了:
```python
# 不过是一个 N 叉树的遍历问题而已
def dp(n):
    for coin in coins:
        dp(n - coin)
```
其实很多动态规划问题就是在遍历一棵树，你如果对树的遍历操作烂熟于心，起码知道怎么把思路转化成代码，也知道如何提取别人解法的核心思路。

再看看回溯算法，前文回溯算法详解干脆直接说了，回溯算法就是个 N 叉树的前后序遍历问题，没有例外。

比如 N 皇后问题吧，主要代码如下：
```java
void backtrack(int[] nums, LinkedList<Integer> track) {
    if (track.size() == nums.length) {
        res.add(new LinkedList(track));
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        if (track.contains(nums[i]))
            continue;
        track.add(nums[i]);
        // 进入下一层决策树
        backtrack(nums, track);
        track.removeLast();
    }

/* 提取出 N 叉树遍历框架 */
void backtrack(int[] nums, LinkedList<Integer> track) {
    for (int i = 0; i < nums.length; i++) {
        backtrack(nums, track);
}
```
N 叉树的遍历框架，找出来了把～你说，树这种结构重不重要？

<font color="deepPink">综上，对于畏惧算法的朋友来说，可以先刷树的相关题目，试着从框架上看问题，而不要纠结于细节问题。</font>

纠结细节问题，就比如纠结 i 到底应该加到 n 还是加到 n - 1，这个数组的大小到底应该开 n 还是 n + 1 ？

<font color="deepPink">从框架上看问题，就是像我们这样基于框架进行<b>抽取和扩展</b>，既可以在<b>看别人解法时快速理解核心逻辑，也有助于找到我们自己写解法时的思路方向</b>。</font>

当然，如果细节出错，你得不到正确的答案，但是只要有框架，你再错也错不到哪去，因为你的方向是对的。

但是，你要是心中没有框架，那么你根本无法解题，给了你答案，你也不会发现这就是个树的遍历问题。

这种思维是很重要的，动态规划详解中总结的找状态转移方程的几步流程，有时候按照流程写出解法，说实话我自己都不知道为啥是对的，反正它就是对了。。。

<font color="deepPink">这就是框架的力量，能够保证你在快睡着的时候，依然能写出正确的程序；就算你啥都不会，都能比别人高一个级别。</font>


## 五、总结

数据结构的基本存储方式就是链式和顺序两种，基本操作就是增删查改，遍历方式无非迭代和递归。

刷算法题建议从「树」分类开始刷，结合框架思维，把这几十道题刷完，对于树结构的理解应该就到位了。这时候去看回溯、动规、分治等算法专题，对思路的理解可能会更加深刻一些。

## 六、参考和学习干货

-  [Data Structure Intro](https://www.youtube.com/watch?v=bum_19loj9A)

-  [Crash Course Computer Science](https://www.youtube.com/watch?v=DuDz6B4cqVc&feature=youtu.be)

- [Data Structures Easy to Advanced Course - Full Tutorial from a Google Engineer and ACM ICPC World Finalist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu)  

- [Data Structures Reference for coding interviews](https://www.interviewcake.com/data-structures-reference)

- [Commonly asked questions](https://www.geeksforgeeks.org/commonly-asked-data-structure-interview-questions-set-1/)

- [Interview tips: Data structure](https://yangshun.github.io/tech-interview-handbook/algorithms/array)

> If you are interested in how data structures are implemented, check out [Lago](https://github.com/yangshun/lago), a Data Structures and Algorithms library for JavaScript. 
