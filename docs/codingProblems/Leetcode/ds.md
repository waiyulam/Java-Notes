
## 一、数组系列
### 数组解题思路总结

#### 1.暴力法
暴力法往往简单易想，当然其效率往往不是最好的，但是如果实现想不出优秀的方案，最好还是写出暴力法的解决方法，并且有总比没有好

#### 2. 双指针

双指针是泛用性最强的一个算法，其主要适用于数组中从前往后，或从后往前的数据交换过程，通过前后两个/首尾两个指针指向不同的数据，来进行数据的交换或处理。

- 双指针思想： 所谓双指针，指的是在遍历对象的过程中，不是普通的使用单个指针进行访问，而是使用两个相同方向或者相反方向的指针进行扫描，从而达到相应的目的。换言之，双指针法充分使用了数组单调性这一特征，从而在某些情况下能够简化一些运算。

不同的指针会带着不同的目的遍历数组

- 快慢指针思想： 快慢指针是同一边开始，两个指针快慢不一样。快慢指针还可以用于找数组的中间位置元素，比如慢指针走一步，快指针都两步，当快指针走到最后一个元素时，慢指针正好指向中间位置的元素。或者可以用来区分数组两种特性的元素比如数组中非零元素和零元素，数组中奇数和偶数等

> 需要注意的是快慢指针会改变原始数组元素的排序方式
> 对于数据单调性有要求的题目我们会使用双指针的方式将元素插入到新的数组中

<p align="center">

<img width="600px" src= "https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/Figures/Array_Explore/Array_Basics_Conclusion_1.png">

</p>

#### 3.逻辑特性分析法
之所以我选择这个名字，是因为这里面的算法泛用性没有那么强，往往是针对不同问题的不同逻辑性来实现解决方案的，具体有：
（1）位运算方法：比如抑或运算在去除相同数字时相当好用；
（2）波峰波谷法：这是一个泛称，主要是针对类似股票买入卖出、山峰积水等问题的统称，其往往与波峰和波谷有直接关联，其主要思想有两种，一是考虑当前问题的逻辑特性，找到其本质所在（如股票买入卖出其实就是大减小），二是需要结合前后波峰波谷的数值，来实现操作；
（3）排序算法结合法：排序算法中的思想如快速排序、归并排序、堆排序与冒泡排序等，其思想可以借鉴到大量数组操作上，如冒泡用于交换，快排归并用于查找。

#### 4.四矩阵法
四矩阵法主要用于数组矩阵的旋转问题之类，其思想在于将矩阵本身分为从外到内的多个n*1的小矩阵，然后再考虑问题的解决方案。具体有两种：
（1）风车图形法：外层大循环实现风翼内缩，内层小循环实现风翼的绘制，最终的一步为风翼在内部的根点连接，从而解决问题；
（2）梯形矩阵逼近法：外部大循环用于内缩，而在内部的小循环实现一整圈的四矩阵交换，在完成一层循环后，内层循环的上限-1且下限+1，从而实现梯形逼近，解决问题。

### 数组解题技巧总结

1. 当我们需要在数组中进行插入和删除操作的时候我们需要优先考虑在数组末尾进行操作，因为这样的操作无需考虑数据搬移的问题从而可能获得时间复杂度为O（1）的算法操作

3. 逆向思维： 有时候从尾部开始寻找能够帮助我们减少代码复杂度或者时间成本，因为有时候从头部开始寻找的时候需要额外判断特殊情况。

4. 删除操作我们需要维护一个自己数组的长度 

### 数组解题框架模板总结

#### 查找

- **线性查找**

1. 从线性数据表中的第一个（或者最后一个）记录开始查找。
2. 以此将记录的关键字与查找的关键字进行比较。
    - 当某个记录的关键字与查找关键字相等的时候，即查找成功。
    - 反之，查完所有记录都没有与之相等的关键字，则查找失败。

> 如何处理越界的问题

- **二分查找**

1. 先将表的中间位置记录的关键字与查找关键字比较。
    - 如果两者相等，则查找成功。
    - 如果不等，则将表分为两个部分，根据比较结果，决定查找哪个子表。

```java
int binarysearch(vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
        int middle = (left + right) / 2;
        if (nums[middle] == target) {
            return middle;
        }
        else if (nums[middle] < target) {
            left = middle + 1;
        }
        else {
            right = middle - 1;
        }
    }return -1;
}
```

> 注意当数组长度为0的时候，找不到元素的时候这两种情况的边界条件

> 熟记二分查找寻找边界

#### 数组内部移位
插入到下标处，在有序表中插入，保持有序性。

```java
int pos1 = 0;//目的位置
//i为开始位置
for(int i =0;i<nums.size();i++){
    //条件
    if(nums[i] != val){
         //数组整体向前移
        nums[pos1++] = nums[i];
    }
}
return pos1;
```

> 注意边界条件需要相应的特殊措施

#### 头尾指针向中间逼近
经典的找和的问题都可以从这种思路下手，2数之和，3数之和，还注意要区分是寻找值还是索引（寻找索引则不能排序），是否允许有重复，不允许重复时要怎样避开重复值。

```java
int pos1 = 0;
int pos2 = nums.size() - 1;
while (pos1<pos2) {
    //判断条件

    //pos更改条件
    if (nums[pos1]<nums[pos2])
        pos1++;
    else
        pos2--;
}
```

> 注意避开重复值的方法

> 注意什么时候左指针加，什么时候右指针减

### 数组系列练习题汇总
<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|<font color="DeepPink"><b>分类</b></font>
----|-----|------|
<font color="White"><b> [01.最大连续1的个数(485)](codingProblems/Leetcode/problems/485-最大连续1的个数.md)</font>|	EASY	| 数组
<font color="White"><b> [02.统计位数为偶数的数字(1295)](codingProblems/Leetcode/problems/1295-统计位数为偶数的数字.md)</font>|EASY	|	数组:枚举
<font color="White"><b> [03.有序数组的平方(977)](codingProblems/Leetcode/problems/977-有序数组的平方.md)</font>|	EASY	| 双指针
<font color="White"><b> [04.复写零(1089)](codingProblems/Leetcode/problems/1089-复写零.md)</font>|	EASY	| 数组插入元素：双指针
<font color="White"><b> [05.合并两个有序数组(88)](codingProblems/Leetcode/problems/88-合并两个有序数组.md)</font>|	EASY|	数组插入元素：双指针
<font color="White"><b> [06.原地移除元素(27)](codingProblems/Leetcode/problems/27-移除元素.md)</font>|	EASY|	数组删除元素：快慢指针
<font color="White"><b> [07.删除排序数组中的重复项(26)](codingProblems/Leetcode/problems/26-删除排序数组中的重复项.md)</font>|	EASY|	数组删除元素：快慢指针
<font color="White"><b> [08.检查整数及其两倍数是否存在(1346)](codingProblems/Leetcode/problems/1346-检查整数及其两倍数是否存在.md)</font>|	EASY|	数组搜索元素：哈希表
<font color="White"><b> [09.有效的山脉数组(941)](codingProblems/Leetcode/problems/941-有效的山脉数组.md)</font>|	EASY|	数组搜索元素：扫描遍历
<font color="White"><b> [10.将每个元素替换为右侧最大元素(1299)](codingProblems/Leetcode/problems/1299-将每个元素替换为右侧最大元素.md)</font>|	EASY|	数组原址操作：逆序遍历
<font color="White"><b> [11.移动零(283)](codingProblems/Leetcode/problems/283-移动零.md)</font>|	EASY|	数组原址操作：快慢指针
<font color="White"><b> [12.按奇偶排序数组(905)](codingProblems/Leetcode/problems/905-按奇偶排序数组.md)</font>|	EASY|	数组原址操作：快慢指针
<font color="White"><b> [13.高度检查器(1051)](codingProblems/Leetcode/problems/1051-高度检查器.md)</font>|	EASY|	数组计数排序
<font color="White"><b> [14.第三大的数(414)](codingProblems/Leetcode/problems/414-第三大的数.md)</font>|	EASY|	数组计数排序
<font color="White"><b> [15.找到所有数组中消失的数字(448)](codingProblems/Leetcode/problems/448-找到所有数组中消失的数字.md)</font>|	EASY|	数组计数排序
<font color="White"><b> 16.两个数组的交集(350)</font>|		|
<font color="White"><b>17.最长公共前缀(14)</font>|	|
<font color="White"><b>18.买卖股票的最佳时机(122）</font>|	|
<font color="White"><b>19.旋转数组(189）</font>|	|
<font color="White"><b>20.加一(66)</font>	|	|
<font color="White"><b>21.两数之和(1)</font>	|	|
<font color="White"><b>22.三数之和(15)</font>	|	|
<font color="White"><b>23.Z字形变换(6)</font> |        |
### 参考

[LeetCode数组解题模板](https://blog.csdn.net/weixin_30262255/article/details/99888838?biz_id=102&utm_term=%E6%95%B0%E7%BB%84%E8%A7%A3%E9%A2%98&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-99888838&spm=1018.2118.3001.4187)
[LeetCode Arrays101 tutorial](https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3257/)

## 二、链表系列

### 链表系列练习题汇总

<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|<font color="DeepPink"><b>分类</b></font>
----|-----|-------|
<font color="White"><b>01.删除链表倒数第N个节点(19)</font>|		|
<font color="White"><b>02.归并两个有序的链表(21)</font>|	|
<font color="White"><b>03.环形链表(141)</font>|	|
<font color="White"><b>04.两数相加(2)</font>|	|
<font color="White"><b>05.找出两个链表的交点(160)</font>|EASY|
<font color="White"><b>06.链表反转(206)</font>	|EASY|
<font color="White"><b>07.从有序链表中删除重复节点(83)</font>	|	EASY|
<font color="White"><b>08.删除链表的倒数第 n 个节点(19)</font> |MEDIUM|
<font color="White"><b>09.交换链表中的相邻结点(24)</font> |MEDIUM|
<font color="White"><b>10.链表求和(445)</font> |MEDIUM|
<font color="White"><b>11.回文链表(234)</font> |EASY|
<font color="White"><b>12.分隔链表(725)</font> |MEDIUM|
<font color="White"><b>13.链表元素按奇偶聚集(328)</font> |MEDIUM|

## 三、栈和队列系列

### 栈和队列系列练习题汇总

<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|
----|-----|
<font color="White"><b>01.用栈实现队列(232)</font>|	EASY
<font color="White"><b>02.用队列实现栈(225)</font>|	EASY
<font color="White"><b>03.最小值栈(155)</font>|	EASY
<font color="White"><b>04.用栈实现括号匹配(20)</font>|	EASY
<font color="White"><b>05.数组中元素与下一个比它大的元素之间的距离(739)</font>	|MEDIUM
<font color="White"><b>06.循环数组中比当前元素大的下一个元素(503)</font>	|	MEDIUM

## 四、哈希表系列

### 哈希表系列练习题汇总

<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|
----|-----|
<font color="White"><b>01.数组中两个数的和为给定值(1)</font>|	EASY
<font color="White"><b>02.判断数组是否含有重复元素(217)</font>|	EASY
<font color="White"><b>03.最长和谐序列(594)</font>|	EASY
<font color="White"><b>04.最长连续序列(128)</font>|	HARD

## 五、堆和优先队列系列

### 1. 堆和优先队列系列总结

#### Java 中的堆实现

```
<!-- c++ 堆实现 -->
可以直接用优先级队列priority_queue

默认是大顶堆 priority_queue<int> maxheap

小顶堆 priority_queue<int,vector<int>,greater<int>> minheap

也可以使用 multiset (使用multiset的情况一般为 需要从堆中删除元素，因为priority_queue的方法中没有 erase方法)

默认是小顶堆 multiset<int> minheap

大顶堆 multiset<int,greater<int>> maxheap
```

#### 单堆问题
**指通过一个堆就可以解决的问题**
一般这种问题都具有以下特点：

求解第/前 k个最大，最小或是最频繁的元素；都可以使用堆来实现 （而不用通过排序实现）

**模式：**
确定大顶堆还是小顶堆

比如求 第K个最大元素，我们就用 大小为K的小顶堆，遍历数组完毕后，小顶堆堆顶元素即为第K个最大元素

遍历数组，压入小顶堆，判断小顶堆的元素个数，如果大于k，则弹出，保证小顶堆内元素个数始终是 k个

 

对于最频繁或是最不频繁的元素问题：可以首先结合 pair<int,int>对组 通过遍历统计，然后以 对组为 堆中元素进行 入堆

priority_queue<pair<int,int>,vector<pair<int,int>>,less<pair<int,int>>>  maxheap

 

比如：寻找第k个最大元素

求第k个最大元素，我们保留下来前k个最大元素即可，而前k个元素中我们又要最小的一个，所以我们可以使用小顶堆

保证小顶堆元素内个数不超过k即可，因为 随着我们压入元素，堆的大小增大，而小元素 一定在堆顶，所以 当堆的大小超过k时，就会 pop出去小元素，最后堆中剩下前k个大元素

#### 双堆问题
**指通过两个堆相互配合解决问题**

被告知，我们拿到一大把可以分成两队的数字。怎么把数字分成两半？使得：小的数字都放在一起，大的放在另外一半。双堆模式就能高效解决此类问题。然后通过小顶堆寻找最小数据，大顶堆寻找堆中最大数据

这样中位数就可以通过 小顶堆和大顶堆堆顶元素求出

**模式**
比如求 数据流中的 中位数，因为 数据流一直在增加，所以如果采用排序，那么每一次增加元素后均需要再次排序，时间复杂度过高； 由于中位数 只需要知道中间两个数（或一个数）即可求出

我们可以使用 大顶堆 来存储 数据流中的 一半较小元素；用 小顶堆来存储 数据流中的 一般较大元素；

且保证 大顶堆的大小 大于 等于 小顶堆的大小，这样 如果 数据流大小为奇数，则返回 大顶堆 的堆顶元素即可，如果数据流大小为偶数，则 大顶堆和小顶堆元素取平均即可

如何实现？

//已知此时数据流元素个数为2k，大顶堆中存储较小元素，大顶堆存储较大元素

maxheap.push(val);//此时堆顶为大元素

将大元素 压入 小顶堆中

minheap.push(maxheap.top())

maxheap.pop()//从大顶堆中删除

//且要保证 大顶堆的大小不小于 小顶堆大小

while(maxheap.size() < minheap.size()) {将 小顶堆中元素压入大顶堆}

//最后通过验证数据流大小 来求中位数即可

### 2. 堆和优先队列题目框架
堆结构就是 用数组实现的完全二叉树,可以是数组的一部分形成了堆

一般是从0开始到某个下标index形成一个大根堆或者小根堆,堆的大小heapSize=index+1
如果从0下标开始,每个节点i,他的左子节点为:2i + 1,右子节点为:2i + 2, 他的父节点为 (i-1)/2;
排序过程的时间复杂度是O(nlgn)。因为建堆的时间复杂度是O(n)（调用一次）；调整堆的时间复杂度是lgn，调用了n-1次，所以堆排序的时间复杂度是O(nlgn)
java中默认是小根堆 使用lamada表达式可以获得大根堆PriorityQueue queue = new PriorityQueue<>((x, y)->y-x);
queue.offer(0) 入堆 queue.poll() 出堆 queue.peek()堆顶元素
queue.isEmpty() 是否为空
堆实际上就是一个随时能给你最大值的一个数据结构 当你不是想要全部的排序顺序序列的时候可能会有大用途 如top(k)问题

堆的难点在于 你怎么用这个给你排好序的 你个结构 你要拿什么进去做排序

### 3. 堆和优先队列系列练习题汇总

<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|
----|-----|
<font color="White"><b>01.数组中的第K个最大元素(215)</font>|	
<font color="White"><b>02.前 K 个高频元素(347)</font>|	
<font color="White"><b>03.数据流的中位数(295)</font>|	
<font color="White"><b>04.最低加油次数(871)</font>|	

## 六、树系列

### 树系列练习题汇总

<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|<font color="DeepPink"><b>分类</b></font>
----|-----|------|
<font color="White"><b>01.最大深度与DFS(104)</font>|EASY|递归	
<font color="White"><b>02.平衡树(110)</font>|EASY|递归	
<font color="White"><b>03.两节点的最长路径(543)</font>|EASY|递归
<font color="White"><b>04.层次遍历与BFS(102)</font>|	EASY|递归
<font color="White"><b>05.BST与其验证(98)</font>|	EASY|递归
<font color="White"><b>06.BST 的查找(700)</font>|	EASY|递归
<font color="White"><b>07.BST 的删除(450)</font>	|	EASY|递归
<font color="White"><b>08.完全二叉树(222)</font>	|	EASY|递归
<font color="White"><b>09.二叉树的剪枝(814)</font>	|EASY|递归
<font color="White"><b>10.翻转树(226)</font>|EASY|递归
<font color="White"><b>11.归并两棵树(617)</font>|EASY|递归	
<font color="White"><b>12. 判断路径和是否等于一个数(112)</font>|EASY|递归	
<font color="White"><b>13. 统计路径和等于一个数的路径数量(437)</font>|EASY|递归	
<font color="White"><b>14. 子树(572)</font>	|EASY|递归	
<font color="White"><b>15. 树的对称(101)</font>|EASY|递归	
<font color="White"><b>16.最小路径(111)</font>	|EASY|递归	
<font color="White"><b>17. 统计左叶子节点的和(404)</font>|EASY|递归	
<font color="White"><b>18. 相同节点值的最大路径长度(687)</font>|EASY|递归	
<font color="White"><b>19. 间隔遍历(337)</font>	|MEDIUM|递归
<font color="White"><b>20. 找出二叉树中第二小的节点(671)</font>|EASY|递归	
<font color="White"><b>21. 一棵树每层节点的平均数(637)</font>|EASY|层次遍历
<font color="White"><b>22. 得到左下角的节点(513)</font>|EASY|层次遍历
<font color="White"><b>23. 非递归实现二叉树的前序遍历(144)</font>|MEDIUM|前中后序遍历
<font color="White"><b>24. 非递归实现二叉树的后序遍历(145)</font>|MEDIUM|前中后序遍历
<font color="White"><b>25. 非递归实现二叉树的中序遍历(94)</font>|MEDIUM|前中后序遍历
<font color="White"><b>26. 修剪二叉查找树(322)</font>|EASY|二叉查找树
<font color="White"><b>27. 寻找二叉查找树的第 k 个元素(230)</font>|MEDIUM|二叉查找树
<font color="White"><b>28. 把二叉查找树每个节点的值都加上比它大的节点的值(538)</font>|EASY|二叉查找树
<font color="White"><b>29. 二叉查找树的最近公共祖先(235)</font>|EASY|二叉查找树
<font color="White"><b>30. 二叉树的最近公共祖先(236)</font>|MEDIUM|二叉查找树
<font color="White"><b>31. 从有序数组中构造二叉查找树(108)</font>|EASY|二叉查找树
<font color="White"><b>32. 根据有序链表构造平衡的二叉查找树(109)</font>|MEDIUM|二叉查找树
<font color="White"><b>33. 在二叉查找树中寻找两个节点，使它们的和为一个给定值(653)</font>|EASY|二叉查找树
<font color="White"><b>34. 在二叉查找树中查找两个节点之差的最小绝对值(530)</font>|EASY|二叉查找树
<font color="White"><b>35. 寻找二叉查找树中出现次数最多的值(501)</font>|EASY|二叉查找树
<font color="White"><b>36. 实现一个 Trie(208)</font>|MEDIUM|前缀树
<font color="White"><b>37.实现一个 Trie，用来求前缀和(677)</font>|MEDIUM|前缀树



## 七、字符串系列

### 字符串系列练习题汇总

<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|
----|-----|
<font color="White"><b>01.反转字符串(344)</font>|		
<font color="White"><b>02.字符串中的第一个唯一字符(387)</font>|	
<font color="White"><b>03.实现 Sunday 匹配</font>|	
<font color="White"><b>04.大数打印</font>|	
<font color="White"><b>05.验证回文串(125)</font>	|	
<font color="White"><b>06.KMP 精讲</font>	|	
<font color="White"><b>07.旋转字符串(796)</font>	|	
<font color="White"><b>08.最后一个单词的长度(58)</font>	|	
<font color="White"><b>09.两个字符串包含的字符是否完全相同(242)</font>	|EASY
<font color="White"><b>10.计算一组字符集合可以组成的回文字符串的最大长度(409)</font>	|EASY
<font color="White"><b>11.字符串同构(205)</font>	|EASY
<font color="White"><b>12.回文子字符串个数(647)</font>	|MEDIUM
<font color="White"><b>13.判断一个整数是否是回文数(9)</font>	|EASY
<font color="White"><b>14.统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数(696)</font>	|EASY


## 八、数组与矩阵系列

### 数组与矩阵系列练习题汇总

<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|
----|-----|
<font color="White"><b>01.把数组中的 0 移到末尾(283)</font>|EASY		
<font color="White"><b>02.改变矩阵维度(566)</font>|	EASY
<font color="White"><b>03.找出数组中最长的连续 1(485)</font>|EASY
<font color="White"><b>04.有序矩阵查找(240)</font>|	MEDIUM
<font color="White"><b>05.有序矩阵的 Kth Element(378)</font>	|	MEDIUM
<font color="White"><b>06.一个数组元素在 [1, n] 之间，其中一个数被替换为另一个数，找出重复的数和丢失的数(645)</font>	|	EASY
<font color="White"><b>07.找出数组中重复的数，数组值在 [1, n] 之间(287)</font>	|	MEDIUM
<font color="White"><b>08.数组相邻差值的个数(667)</font>	|	MEDIUM
<font color="White"><b>09.数组的度(697)</font>	|EASY
<font color="White"><b>10.对角元素相等的矩阵(766)</font>	|EASY
<font color="White"><b>11.嵌套数组(565)</font>	|MEDIUM
<font color="White"><b>12.分隔数组(769)</font>	|MEDIUM
<font color="White"><b>13.判断一个整数是否是回文数(9)</font>	|EASY
<font color="White"><b>14.统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数(696)</font>	|EASY


## 九、图系列

### 图系列练习题汇总

<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|<font color="DeepPink"><b>分类</b></font>
----|-----|------|
<font color="White"><b>01.判断是否为二分图(785)</font>|MEDIUM|二分图	
<font color="White"><b>02.课程安排的合法性(207)</font>|MEDIUM|拓扑排序	
<font color="White"><b>03.课程安排的顺序(210)</font>|MEDIUM|拓扑排序	
<font color="White"><b>04.冗余连接(684)</font>|	MEDIUM|并查集

## 十、位运算系列

### 位运算系列汇总


<font color="DeepPink"><b>题目</b></font>|<font color="DeepPink"><b>难度</b></font>|
----|-----|
<font color="White"><b>01.使用位运算求和</font>|		
<font color="White"><b>02.判断一个数是不是 2 的 n 次方(231)</font>|	EASY
<font color="White"><b>03.返回一个数二进制中1的个数</font>|	
<font color="White"><b>04.只出现一次的数字</font>|	
<font color="White"><b>05.只出现一次的数字Ⅱ</font>	|	
<font color="White"><b>06.找出数组中缺失的那个数(268)</font>	|	EASY
<font color="White"><b>07.统计两个数的二进制表示有多少位不同(461)</font>	|	EASY
<font color="White"><b>08.数组中唯一一个不重复的元素(136)</font>	|	EASY
<font color="White"><b>09.数组中不重复的两个元素(260)</font>	|MEDIUM
<font color="White"><b>10.翻转一个数的比特位(190)</font>	|EASY
<font color="White"><b>11.不用额外变量交换两个整数</font>	|???
<font color="White"><b>12.判断一个数是不是 4 的 n 次方(342)</font>	|EASY
<font color="White"><b>13.判断一个数的位级表示是否不会出现连续的 0 和 1(693)</font>	|EASY
<font color="White"><b>14.求一个数的补码(476)</font>	|EASY
<font color="White"><b>15.实现整数的加法(371)</font>	|EASY
<font color="White"><b>16.字符串数组最大乘积(318)</font>	|MEDIUM
<font color="White"><b>17.统计从 0 ~ n 每个数的二进制表示中 1 的个数(338)</font>	|MEDIUM



