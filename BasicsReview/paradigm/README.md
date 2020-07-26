# Programming paradigm
Paradigms |Intuition| Practices
---|---|---
[Divide and Conquer](#Divide-and-Conquer-algorithms)|把一个复杂的问题分成两个或更多的相同或相似的子问题，直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并 <br> DAC breaks a problem into subproblems that are similar to the original problem, recursively solves the subproblems, and finally combines the solutions to the subproblems to solve the original problem.|<ul><li> [Binary Search](DAC/binary_search.py)</li><li>[Majority Element](DAC/majority_element.py)</li><li>[Max Subarray](DAC/max_subarray.py)</li><li>[Merge sort](DAC/merge_sort.py)</li><li>[Quick sort](DAC/quicksort.py)</li>
[Greedy Algorithms](#Greedy-Algorithms)|<p>一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是最好或最优的算法 <br>Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit</p> | <ul><li>[Travelling salesman](https://en.wikipedia.org/wiki/Travelling_salesman_problem)</li><li>[huffman coding](https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/)</li></ul>
[Backtracking](#Backtracking)|<p>在解决约束满足问题时，我们逐步构造更多的候选解，并且在确定某一部分候选解不可能补全成正确解之后放弃继续搜索这个部分候选解本身及其可以拓展出的子候选解，转而测试其他的部分候选解<br>Backtracking is solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.</p>|<ul><li>[Hamiltonian Cycle](BRUTEFORCE/backtracking/hamiltonian.py)</li><li>[Graph Coloring](BRUTEFORCE/backtracking/m_coloring.py)</li><li>[Sum of subsets](BRUTEFORCE/backtracking/sum_subset.py)</ul>
[Branch and Bound](#Branch-and-bound)|<p>对有约束条件的最优化问题的所有可行解（数目有限）空间进行搜索，该算法在具体执行时，把全部可行的解空间不断分割为越来越小的子集（称为分支），并为每个子集内的解的值计算一个下界或上界（称为定界）<br>branch and bound estimate a  bound on best possible solution subtree rooted with every node. If the estimate best solution in subtree is worse than current best, we can simply ignore this node and its subtrees and reach the solution faster.</p>|<ul><li>[0/1 Knapsack](BRUTEFORCE/brand_bound/knapsack.py)</li><li>[Traveling Salesman](BRUTEFORCE/brand_bound/tsp.py)
[Dynamic Programming](#Dynamic-Programming-and-memoization)|<p>通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法，适用于有重叠子问题和最优子结构性质的问题<br>Dynamic Programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and stores the results of subproblems to avoid computing the same results again</p>|[DP problems](DP)

## Table of Contents 
+ [Divide and Conquer](#Divide-and-Conquer-algorithms)

+ [Greedy Algorithms](#Greedy-Algorithms)

+ [Backtracking & Branch and Bound](#Backtracking-and-Branch-and-Bound)

+ [Big Guy: Dynamic Programming and memoization 😭](#Dynamic-Programming-and-memoization)

 
## Divide and Conquer algorithms

- **Definition** : 

```markdown
DAC breaks a problem into subproblems that are similar to the original problem, recursively solves the subproblems, and finally combines the solutions to the subproblems to solve the original problem. Because DAC solves subproblems recursively, each subproblem must be smaller than the original problem, and there must be a base case for subproblems.
```

> * Divide the problem into a number of subproblems that are smaller instances of the same problem.
> * Conquer the subproblems by solving them recursively. If they are small enough, solve the subproblems as base cases.
> * Combine the solutions to the subproblems into the solution for the original problem.

<p align="center">
  <img width="460" height="300" src="https://cdn.kastatic.org/ka-perseus-images/db9d172fc33b90e905c1213b8cce660c228bb99c.png">
</p>

- **Tutorials**: 
  -  [x] [Video no. 18, 33 to 38 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)
  -  [ ] Chapter 4 | Divide and Conquer | Page No.65 from Introduction to Algorithm by CLRS
  -  [x] Implement DAC algorithms : [major element](https://leetcode.com/problems/majority-element/solution/), maximum subarray sum, merge sort, binary search, quick sort
  	-  [Geeksforgeeks](https://www.geeksforgeeks.org/divide-and-conquer-algorithm-introduction/)
	-  [Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/divide-and-conquer-algorithms)

-------------------------------------------------------------------------------------------------------- 

## Greedy Algorithms

- **Definition**: 

```markdown
Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. It follows the problem-solving heuristic of making the locally optimal choice** at **each stage** with the **intent of finding a global optimum**. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time. So the problems where choosing locally optimal also leads to global solution are best fit for Greedy.
```

- **Examples: travelling salesman**:  

The greedy strategy for the travelling salesman problem (which is of a high computational complexity) is the following heuristic: "At each step of the journey, visit the nearest unvisited city." This **heuristic** does not intend to find a best solution, but it **terminates in a reasonable number of steps**; finding an optimal solution to such a complex problem typically requires unreasonably many steps. 

In mathematical optimization, greedy algorithms optimally solve combinatorial problems having the properties of matroids, and give constant-factor approximations to optimization problems with submodular structure.
 
- **Tutorials**:
  -  [x] [Video no.39-no.45 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)   
Proofing greedy algorithm is quite difficult. Studying known problems like knapsack, job schedule, optimal merge pattern, Huffman coding etc are enough to ace greedy questions.
  -  [ ] [Geeks: Greedy Algorithms](https://www.geeksforgeeks.org/greedy-algorithms/)

--------------------------------------------------------------------------------------------------------   

## Backtracking and Branch and Bound

BNB and Backtracking are better than naive brute force approach (generating all possible combinations of digits and then trying every combination one by one) as it drops a set of permutations whenever it fail to satisfy the constraints. The **bounding function** is the condition to check if node get kill or be selected.  

### Backtracking

- **Definition**: 

```markdown
**Backtracking** is used when you have **multiple solutions** and you want those solution answers. Backtracking is solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.  
```

> - In the tree representation, we can do DFS of solution tree
> - If we reach a point where a solution no longer is feasible, there is no need to continue exploring.

### Branch and bound

- **Definition** 

```markdown
**Branch and bound** is an algorithm design paradigm which is generally used for solving combinatorial **optimization** problems. These problems typically exponential in terms of time complexity and may require exploring all possible permutations in worst case. The backtracking based solution works better than brute force by **ignoring infeasible solutions**. But BnB can do better (than backtracking) if we can estimate a **bound on best possible solution subtree rooted with every node**. 
```
> - Estimate a **bound on best possible solution subtree rooted with every node**
> - If the estimate best solution in subtree is worse than current best, we can simply ignore this node and its subtrees and reach the solution faster.

- **Ways to implement**: 

There are also three ways to implement branch and bound approach which are **stack, queue, and leastcost**. For leastcost approach, instead of generating entire tree, we always pcik up the node that is least cost and explore that one. It turns out that it is easier to reach the minimization solution quickly compared to other two. (Depends on problems) Branch and bound is very useful technique for searching a solution but in worst case, we need to fully calculate the entire tree. At best, we only need to fully calculate one path through the tree and prune the rest of it.

### BNB v.s. Backtracking 

Both follow Brute force approach and both generate state space tree but in different ways. Backtraking is implemented in **depth-wise(DFS)** and Branch & Bound is implemented in **level-wise(BFS)**. While branch and bound has similar approachs as backtracking in some sense, brand and bound is more useful to find the optimal solution ( e.g. minimization problems ). 

- **Tutorials**: 
  -  [x] [Video no.63 to no.71 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O). 
  -  [x] Practices the following problem 
  - [Hamiltonian Cycle Problem using backtracking](https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/)
  - [Graph Coloring Problem using backtracking](https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/)
  - [Sum of subsets Problem using backtracking](https://www.geeksforgeeks.org/subset-sum-backtracking-4/)
  - [0/1 Knapsack Problem using BnB](https://www.geeksforgeeks.org/0-1-knapsack-using-branch-and-bound/)
    - [Implementation](https://www.geeksforgeeks.org/implementation-of-0-1-knapsack-using-branch-and-bound/)
    - [Video](https://www.youtube.com/watch?v=slayHO7gKEQ)
  - [Traveling Salesman using BnB](https://www.techiedelight.com/travelling-salesman-problem-using-branch-and-bound/)

- **[Practices](BRUTEFORCE)**

--------------------------------------------------------------------------------------------------------   

## Dynamic Programming and memoization

### Dynamic Programming Intro : Recognize the pattern/formula for a dp problem
Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial. Now one of the most important study material for DP. How many of us know that a dynamic programming is nothing but a **topological sort of problem dependency directed acyclic graph** which means if you can generate a *test case for a DP problem that has a cycle then that DP solution will fail for that cyclic graph*. If some problem instances can be seen as pieces of other problem instances, we can store our work along the way to avoid doing the same work. One way to think of DP is "careful/clever brute force" while trying out all possible solutions and get polynomial time if do it carefully. Then **DP = "GUESSING" + "RECURSION" + "MEMOIZATION"**. The main challenge for using DP paradigm is to identify the subproblems and guess the possible solution for part of the problem.   
To know all of this cool things and understand DP really good then study:    

  -  [x] [Intro](https://www.youtube.com/watch?v=iv_yHjmkv4I)  
  -  [x] [video no.19(MUST MUST!),20-22 from MIT OCW Introduction to Algorithm](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
  -  [x] [Dynamic Programming Fundamentals](https://www.geeksforgeeks.org/dynamic-programming/)
  -  [x] [Steps to solve DP problems](https://www.geeksforgeeks.org/solve-dynamic-programming-problem/)
  -  [x] [DP vs. DAC](https://www.geeksforgeeks.org/dynamic-programming-vs-divide-and-conquer/?ref=rp)    
![](https://media.geeksforgeeks.org/wp-content/uploads/01-DP-vs-DC-DP-vs-DC-diagram-1024x492.png)

**Dynamic Programming Prerequisites/Restrictions**
As we’ve just discovered there are two key attributes that divide and conquer problem must have in order for dynamic programming to be applicable.:
1. **Optimal substructure** : optimal solution can be constructed from optimal solutions of its subproblems
2. **Overlapping sub-problems** : problem can be broken down into subproblems which are reused several times or a recursive algorithm for the problem solves the same subproblem over and over rather than always generating new subproblems       

Once these two conditions are met we can say that this divide and conquer problem may be solved using dynamic programming approach.    
Dynamic programing is based on divide and conquer principle and may be applied only if the problem has overlapping sub-problems and optimal substructure (like in Levenshtein distance case). Dynamic programming then is using memoization or tabulation technique to store solutions of overlapping sub-problems for later usage.      

#### Memoization and tabulation 
Memoization (top-down cache filling) refers to the technique of caching and reusing previously computed results. 
  -  [x] [HackerRank: DP & Memoization](https://www.youtube.com/watch?v=P8Xa2BitN3I&t=13s)
  -  [x] [What is memoization and how can I use it in Python?](https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python)     
  
#### Problems Practices: happy coding ~
*Anyway, you have to study known DP problems as much as you possibly can and try to recognize the **patterns and types***.       
  -  [ ] [Leetcode Coin(giveaway) winning post on Dynamic Programming Patterns by aatalyk](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)    
       
Study and solve all questions from here. Just stick with it till the last question of this article. And when studying the article try to follow:       
  -  [ ] [Tushar Roy's Dynamic Programing Playlist](https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr)
  -  [ ] [Video no.46 to no.60 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)        
  
I find Abdul bari's tutorial more effective and easy to follow. His style to teach students is quite exceptional. Suppose you are studying *Longest Common Subsequence*    
1. **understand the question** really good 
2. try to **solve a small problem** of the main problem 
3. try to solve a bit big problem with the help of solution and see if you can **find any formula/pattern** 
4. if you can't find any then read **is discussion/solution(only algorithm not code)** and try to **code it up** after understanding 
5. If still doesn't work for you then **watch the video of that topic from the playlist i have mentioned** and try hard this time to understand and visualize the algorithm. 
6. You solved a DP Question! Yahoo!.
  
#### Tips and Others
- **Pythonistas** After you just come up with a 2N backtracking solution just use functools.lru_cache(maxsize=None) decorator and you will have a dp solution(almost 90% time).Say for example: A String based DP problem involves a 2D matrix where [i][j] generally refers to the solution for index i to j of the String and etc. Here is what you should do, try to understand backtracking very well as that will be the key in solving DP. After getting a backtracking solution you can memoize the previous solutions and reduce solutions to 2/3 Degree Polynomial Time.    
  -  [ ] [Cheat Sheet](https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/) 
  -  [ ] [26-27,39-45 from MIT OCW Introduction to Algorithm](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
  