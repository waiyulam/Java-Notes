# Interview-Prep-Guide
Cracking the interview : Interviewing can be tough because you can feel like you are making no progress. Having this study guide will help you track your progress and give you a better read on how you are doing!    
Don't Rush. Enjoy the journey. Try to be a natural problem solver not a interview acing problem solver. And you are not alone!  
**Keep moving mate, never ever dare to give up. Hard work is going to pay you off very soon.**

![](https://media.giphy.com/media/KWQy384u0Rn9bCvwMa/giphy.gif)

##  Regular Deliberate Strategic Practice
### Retaining Computer Science Knowledge
1. Review cs fundamentatals and make [FlashCards](https://github.com/jwasham/computer-science-flash-cards) for main points. Review the flash cards when you have time 
2. Start doing coding interview questions while you're learning data structures and algorithms. 
3. Review
 
### Keep Practics when you get this point 
1. Use Leetcode to practices different problems 
2. Take a break from programming problems for a half hour and go through your flashcards.

## Coding problem practice 
- problem recognition, and where the right data structures and algorithms fit in
- gathering requirements for the problem
- talking your way through the problem like you will in the interview
- coding on a whiteboard or paper, not a computer
- coming up with time and space complexity for your solutions
- testing your solutions
## Daily Plan 
1. [ ] CS Foundamentals Prep 
	- Take one subject from the list below, watch videos about that subject, and write an implementation 
	- [Implementation Category of Hackerrank](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=implementation&badge_type=problem-solving)
	- Each subjet should implement in at least 10 questions (Java / Python )
	- Each problems should follow the [template](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Leetcode)
2. [ ] Run with practice problems 
	- Leetcode ( Eash -> **Medium** -> Hard )
	- Make use of built-in types
	- Each problems should follow the [template](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Leetcode)
	
# Table of Contents 
- [CS Fundamentals](#CS-Funamentals)
	* [Introduction to Algorithms](#Introduction-to-Algorithms)
		+ [Time&Space Complexity](#Time-and-Space-Complexity)
		+ [Recursion](#Recursion-and-analysis-of-recurrence-relations)
		+ [Divide and Conquer](#Divide-and-Conquer-algorithms)
		+ [Greedy Algorithms](#Greedy-Algorithms)
		+ [Backtracking & Branch and Bound](#Backtracking-and-Branch-and-Bound)
	* [Data Structures](#Data-Structures)
	* [Algorithms](#Algorithms)
	* [Best DSA study Link](#Best-DSA-study-Link)
- [Run practice problems](#Run-practice-problems)
- [Interview Questions](#Interview-Questions)
- [Programming Language Review](#Programming-Language-Review)
- [Others](#Others)

# CS Fundamentals 
## Introduction to Algorithms 
### Time and Space Complexity
--------------------------------------------------------------------------------------------------------   
  -  [x] [Video no. 1-16 Abdul Bari's Algorithm Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)  
ps:After watching this 16 videos i can guarantee that you will gain mastery on Time Complexity for sure.)  

  -  [ ] [Overall Recall of Algorithm Complexity Analysis](http://discrete.gr/complexity/)
  -  [ ] [Cheat Sheet](http://bigocheatsheet.com/)
  
### Recursion and analysis of recurrence relations
--------------------------------------------------------------------------------------------------------   
  -  [x] [Recursion Playlist by mycodeschool](https://www.youtube.com/playlist?list=PL2_aWCzGMAwLz3g66WrxFGSXvSsvyfzCO)
  -  [x] [Masters Theorem for the proof of recursion: video no. 18 to no. 29 ](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)    
  
**Understand types of recursion like tail, head, nested, tree(the one you need everywhere) etc**
  -  [x] [Sparknotes tutorial on recursion types](https://www.sparknotes.com/cs/recursion/whatisrecursion/section2/) 
  -  [x] [Types of recursion part 1 (video)](https://www.youtube.com/watch?v=t9whckmAEq0)
  -  [x] [Types of recursion part 2 (video)](https://www.youtube.com/watch?v=HIt_GPuD7wk)
  
**How is tail recursion better than not?**
  -  [x] [What Is Tail Recursion Why Is It So Bad?](https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad)
  -  [x] [Tail Recursion vs Head Recursion (video )](https://www.youtube.com/watch?v=lG6HxO7cDRw)  

Space consumed by recursive functions is expensive. Beside using recursion for more element and simple code, we should take this into consideration and be aware of how to optimize the solution for better performance. For example, if the function only ends at calling itself, we might consider that is there any iterative method to solve it. 

**Iterative vs. Recursive**   
Recursion is made for solving problems that can be broken down into smaller, repetitive problems. It is especially good for working on things that have many possible branches and are too complex for an iterative approach. For iterative approach, we are solving problem from bottom to up but for resursive approach, we are solving problem in top-down method. But sometimes problem are too complex to be solved iteratively such as searching in file system. Trees and graphs are data structures that recursion is the best and easiest way to do traversal and Recursion works well for this type of structure because you can search multiple branching paths without having to include many different checks and conditions for every possibility..
-  [x] [When to Loop? When to Recurse?](https://medium.com/better-programming/when-to-loop-when-to-recurse-b786ad8977de)
-  [x] [What is recursion and when should I use it?](https://stackoverflow.com/questions/3021/what-is-recursion-and-when-should-i-use-it) 
-  [x] [When resursion is useful](https://www.quora.com/Is-recursion-actually-useful-I-cant-find-any-reason-to-use-it-Why-do-some-people-love-to-use-it)

Almost everyone knows what recursion is, right? But that is not enough. You have to create some sort of mental model how recursion actually saves states by pushing function code to stack and reaches at the last/smallest problem and then solves it and then backtrack from there by poping function code from stack to top and etc. You have to spend sufficient time to understand recursion through studying and practicing, as recursion is will be the base of everything in this type.

### Divide and Conquer algorithms
--------------------------------------------------------------------------------------------------------   
**Paradigm** : DAC breaks a problem into subproblems that are similar to the original problem, recursively solves the subproblems, and finally combines the solutions to the subproblems to solve the original problem. Because DAC solves subproblems recursively, each subproblem must be smaller than the original problem, and there must be a base case for subproblems.
* Divide the problem into a number of subproblems that are smaller instances of the same problem.
* Conquer the subproblems by solving them recursively. If they are small enough, solve the subproblems as base cases.
* Combine the solutions to the subproblems into the solution for the original problem.
![](https://cdn.kastatic.org/ka-perseus-images/db9d172fc33b90e905c1213b8cce660c228bb99c.png)

  -  [x] [Video no. 18, 33 to 38 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)
  -  [ ] Chapter 4 | Divide and Conquer | Page No.65 from Introduction to Algorithm by CLRS
  -  [x] Implement DAC algorithms : [major element](https://leetcode.com/problems/majority-element/solution/), maximum subarray sum, merge sort, binary search, quick sort
  	-  [Geeksforgeeks](https://www.geeksforgeeks.org/divide-and-conquer-algorithm-introduction/)
	-  [Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/divide-and-conquer-algorithms)
  
### Greedy Algorithms
-------------------------------------------------------------------------------------------------------- 
A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the **locally optimal choice** at **each stage** with the **intent of finding a global optimum**. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.    

For example, a greedy strategy for the travelling salesman problem (which is of a high computational complexity) is the following heuristic: "At each step of the journey, visit the nearest unvisited city." This **heuristic** does not intend to find a best solution, but it **terminates in a reasonable number of steps**; finding an optimal solution to such a complex problem typically requires unreasonably many steps. In mathematical optimization, greedy algorithms optimally solve combinatorial problems having the properties of matroids, and give constant-factor approximations to optimization problems with submodular structure.
 
  -  [x] [Video no.39-no.45 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)   
Proofing greedy algorithm is quite difficult. Studying known problems like knapsack, job schedule, optimal merge pattern, Huffman coding etc are enough to ace greedy questions.

  -  [ ] [Geeks: Greedy Algorithms](https://www.geeksforgeeks.org/greedy-algorithms/)
  
Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. So the problems where choosing locally optimal also leads to global solution are best fit for Greedy.
  
### Backtracking and Branch and Bound
--------------------------------------------------------------------------------------------------------   
This topic is the key ingredient to solve Dynamic Programming questions. Both follow Brute force approach and both generate state space tree but in different ways. Backtraking is implemented in **depth-wise(DFS)** and Branch & Bound is implemented in **level-wise(BFS)**.    
Backtracking is used when you have **multiple solutions** and you want those solution answers. Backtracking is solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time. This is better than naive approach (generating all possible combinations of digits and then trying every combination one by one) as it drops a set of permutations whenever it backtracks. The **bounding function** is the condition to check if node get kill or be selected.    
While branch and bround is similar to backtracing in the sense that it also use state space tree for solving a problem, it is useful for solving **optimization problem ( only minimization )** and we can convert maximization problem to minimization. The **upper bound and cost** are the conditions to check if the node get killed or selected. Upper bound represents that if we are getting some penality, at most we are getting the "u" for the right solution. In addition, there are also three ways to implement branch and bound approach which are **stack, queue, and leastcost**. For leastcost approach, instead of generating entire tree, we always pcik up the node that is least cost and explore that one. It turns out that it is easier to reach the minimization solution quickly compared to other two. (Depends on problems) 

 -  [x] [Video no.63 to no.71 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O). 
 -  [ ] Practices the following problem 
 	- [Hamiltonian Cycle Problem using backtracking](https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/)
	- Graph Coloring Problem using backtracking 
	- Sum of subsets Problem using backtracking 
	- 0/1 Knapsack Problem using BnB
	- Traveling Salesman using BnB

### Big Guy: Dynamic Programming and memoization 😭
--------------------------------------------------------------------------------------------------------   
Recognize the pattern/formula for a dp problem. Say for example: A String based DP problem involves a 2D matrix where [i][j] generally refers to the solution for index i to j of the String and etc. Here is what you should do, try to understand backtracking very well as that will be the key in solving DP. After getting a backtracking solution you can memoize the previous solutions and reduce solutions to 2/3 Degree Polynomial Time. 

  - [ ] [Intro](https://www.youtube.com/watch?v=iv_yHjmkv4I)
  - [ ] [video no.19(MUST MUST!),20-22,26-27,39-45 from MIT OCW Introduction to Algorithm](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
  -  [ ] [DP & Memoization](https://www.youtube.com/watch?v=P8Xa2BitN3I&t=13s)

Anyway, you have to study known DP problems as much as you possibly can and try to recognize the patterns and types. 
  -  [ ] [Fibonacci, Shortest Paths](https://www.youtube.com/watch?v=OQ5jsbhAv_M&t=7s) : Dijkstron & Floyd Warshall
  -  [ ] [Text Justification, Blackjac](https://www.youtube.com/watch?v=ENyox7kNKeY&t=4s)
  -  [ ] [Leetcode Coin(giveaway) winning post on Dynamic Programming Patterns by aatalyk](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
  -  [ ] [Tushar Roy's Dynamic Programing Playlist](https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr)
  -  [ ] [Video no.46 to no.60 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)
  -  [ ] [DP vs. DAC](https://www.geeksforgeeks.org/dynamic-programming-vs-divide-and-conquer/?ref=rp)
  -  [ ] [Cheat Sheet](https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/)
  
**Comment**: I find **Abdul bari's tutorial** more effective and easy to follow. His style to teach students is quite exceptional. Suppose you are studying Longest Common Subsequence, first understand the question really good -> try to solve a small problem of the main problem -> try to solve a bit big problem with the help of solution and see if you can find any formula/pattern -> if you can't find any then read discussion/solution(only algorithm not code) and try to code it up after understanding -> If still doesn't work for you then watch the video of that topic from the playlist i have mentioned and try hard this time to understand and visualize the algorithm. -> You solved a DP Question!   

**Tips**: **Pythonistas** After you just come up with a 2N backtracking solution just use functools.lru_cache(maxsize=None) decorator and you will have a dp solution(almost 90% time).

### Graph Theory (directed, undirected, weighted, rooted(IN & OUT) and unrooted tree, DAG etc)
--------------------------------------------------------------------------------------------------------   
- [ ] [Graph Theory Easy to Advanced Course - Full Tutorial from a Google Engineer and ACM ICPC World Finalist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P)

Comment: There are so much overlaps in between greedy, dp with graph theory. Say for example Dijkstra, Prim's and Kruskal's Minimum Spanning tree are just Greedy Algorithms or backtracking is just DFS with branch pruning with condition. So you will find it a lot easier after studying programming paradigm section. In fact graph problems are either so easy to recognize that everything is given so explicitly that any one can recognize it as a typical graph question or may be it's too hidden to even think it as a graph question. So my suggestion is to think out of the box for a problem, think if a problem can be solved by using graphs. **Never forget that, Interviewers are just obsessed with binary tree, so try to solve as many questions as you can related to tree, specifically binary tree(and also n-ary tree). And also solve at least 20 questions with tag BFS and DFS in Leetcode which will definitely boost your tree and graph problem solving skill as graph traversal is the main toolkit to solve tree/graph problems in interview. That's all about graph.** 

### NP, NP-Complete and Approximation Algorithms
--------------------------------------------------------------------------------------------------------   
  -  [ ] Know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem, and be able to recognize them when an interviewer asks you them in disguise.
  -  [ ] [Video no.72 to no.73 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/watch?v=e2cF8a5aAhE&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=72)
  -  [ ] [Introduction to NP-Completeness](https://youtu.be/qcGnJ47Smlo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=2939)
  -  [ ] [Approximate Greedy Algorithms for NP Complete Problems](https://www.geeksforgeeks.org/greedy-algorithms/#approximateGreedyAlgorthms)

### String Manipulation 
--------------------------------------------------------------------------------------------------------   
  -  [ ] Follow the string section from [CP Algorithms Site](http://cp-algorithms.com/).
  -  [ ] [Longest Consecutive Characters](https://www.youtube.com/watch?v=qRNB8CV3_LU)
  -  [ ] [Substring Search](https://www.coursera.org/learn/algorithms-part2/home/week/4)
  -  [ ] Linear-time string matching: Z algorithm 

### Bit Manipulation 
--------------------------------------------------------------------------------------------------------   
  -  [ ] Follow [HackerEarth Bit Manipulation Tutorial](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/) and also [TopCoder Fun with Bits Tutorial](https://www.topcoder.com/community/competitive-programming/tutorials/a-bit-of-fun-fun-with-bits/).

## Data Structures
![](https://res.cloudinary.com/practicaldev/image/fetch/s--WlnYH5fq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1600/1%2ADyu63sMUVL-gYEZISOE2BQ.jpeg)

[ ] [Data Structures Easy to Advanced Course - Full Tutorial from a Google Engineer and ACM ICPC World Finalist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu)  

ps:This is one of the best materials to study on data structure topic. William implemented each on Java. But it doesn't really matter which language you use, i did this course in both in c++ and python. And try to code yourself after watching a data structure topic and do some leetcode question on that. And this is all you need to ace DS questions.)

### Arrays 
--------------------------------------------------------------------------------------------------------   
  - [ ] [Multi-dim Array](https://archive.org/details/0102WhatYouShouldKnow/02_05-multidimensionalArrays.mp4) 
  - [ ] [Dynamic Array](https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV)
  - [ ] [Resizing Array](https://archive.org/details/0102WhatYouShouldKnow/03_01-resizableArrays.mp4)

### Linked Lists
--------------------------------------------------------------------------------------------------------   
  -  [ ] [Intro](https://www.youtube.com/watch?v=njTh_OwMljA&feature=youtu.be) 
  -  [ ] [Linked Lists vs Array](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9)

### Trees
--------------------------------------------------------------------------------------------------------   
  -  [ ] [Intro](https://www.youtube.com/watch?v=oSWTXtMglKE&feature=youtu.be)

### Heap / Priority Queue / Binary Heap
--------------------------------------------------------------------------------------------------------   
  -  [ ] [Intro](https://www.youtube.com/watch?v=t0Cq6tVNRBA&feature=youtu.be)

### Hash Table
--------------------------------------------------------------------------------------------------------   
  -  [ ] [Intro](https://www.youtube.com/watch?v=shs0KM3wKv8&feature=youtu.be)
  -  [ ] [Phone Book Problem](https://www.coursera.org/learn/data-structures/lecture/NYZZP/phone-book-problem)

### Stacks and Queues
--------------------------------------------------------------------------------------------------------   
  -  [ ] [Intro](https://youtu.be/wjI1WNcIntg)
  -  [ ] [Using Stacks Last-In First-Out ](https://archive.org/details/0102WhatYouShouldKnow/05_01-usingStacksForLast-inFirst-out.mp4)

### Tries
--------------------------------------------------------------------------------------------------------   
  -  [ ] [Intro](https://www.youtube.com/watch?v=zIjfhVPRZCg)

### Others 
--------------------------------------------------------------------------------------------------------   
  -  [ ] [Data Structure Intro](https://www.youtube.com/watch?v=bum_19loj9A)
  -  [ ] [Crash Course Computer Science](https://www.youtube.com/watch?v=DuDz6B4cqVc&feature=youtu.be)


## Algorithms 
![](https://res.cloudinary.com/practicaldev/image/fetch/s--POn2iYyz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://cdn-images-1.medium.com/max/1600/1%2AbPpvELo9_QqQsDz7CSbwXQ.gif) 

### Graph Search
--------------------------------------------------------------------------------------------------------   
  -  [ ] [Intro](https://www.youtube.com/watch?v=zaBhtODEL0w&list=PLX6IKgS15Ue02WDPRCmYKuZicQHit9kFt)
  -  [ ] [BFS(breadth-first search) and DFS(depth-first search)](https://www.youtube.com/watch?v=uWL6FJhq5fM)

### Binary Search 
--------------------------------------------------------------------------------------------------------   
  -  [ ] [Intro](https://youtu.be/P3YID7liBug)
  -  [ ] [Binary Search Tree Review](https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
  
### Sorting
--------------------------------------------------------------------------------------------------------   
-  [ ] [Bubble Sort](https://youtu.be/6Gv8vg0kcHc)
-  [ ] [Merge Sort](https://youtu.be/KF2j-9iSf4Q)
	- [Standard](https://www.geeksforgeeks.org/python-program-for-merge-sort/)
-  [ ] [Quick Sort](https://youtu.be/SLauY6PpjW4)   
	- [Standard](https://www.geeksforgeeks.org/python-program-for-quicksort/)
	- [Median of three](https://github.com/meclark256/Coursera/blob/master/QuickSort.py)
-  [ ] [stability in sorting algorithms](https://www.geeksforgeeks.org/stability-in-sorting-algorithms/)   
	- [quicksort](https://www.geeksforgeeks.org/stable-quicksort/)
-  [ ] [Heap Sort](https://www.youtube.com/watch?v=HqPJF2L5h9U&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=32): Heap sort is great, but not stable.
-  [ ] [sorting analysis in different criterias](https://www.youtube.com/watch?v=ak-pz7tS5DE&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=35)

## Best DSA study Link
  -  [ ] [TopCoder Competitive Programming Tutorials](https://www.topcoder.com/community/competitive-programming/tutorials/)
  -  [ ] [Technical interview Guide by Yangshun](https://yangshun.github.io/tech-interview-handbook/introduction/)
  -  [ ] [HackerEarth CodeMonk(step by step Guide)](https://www.hackerearth.com/practice/codemonk/)
  -  [ ] [Python Algorithms for Interviews](https://www.youtube.com/watch?v=p65AHm9MX80)

# Run practice problems

## [hackerrank](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/hackerrank)
- [ ] [Implementation Category of hackerrank](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=implementation&badge_type=problem-solving)

## [Leetcode](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Leetcode) :
Practices and Practices. only practice can guarantee success
- Easy 
- Medium 
- Hard 

# Interview Questions 
  - [Google Coding Interview --- Universal Value Tree Problem](https://www.youtube.com/watch?v=7HgsS8bRvjo)
  - [Google Coding Interview Question and Answer #1: First Recurring Character ](https://www.youtube.com/watch?v=GJdiM-muYqc)
  - [Find min and max element in a binary search tree ](https://www.youtube.com/watch?v=Ut90klNN264&index=30&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
  - [Find height of a binary tree ](https://www.youtube.com/watch?v=_pnqMz5nrRs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=31)
  - [Check if a binary tree is binary search tree or not](https://www.youtube.com/watch?v=yEwSGhSsT0U&index=35&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
  - [What Is Tail Recursion? Why Is It So Bad?](https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad)
  
# Programming Language Review 
1. Java 
2. Python 
3. C++ 

# Mathmatics Basics  (Number theory, Computational Geometry, Combinatorics, Linear Algebra etc)
--------------------------------------------------------------------------------------------------------   
  - [ ] [MIT 6.042J Mathematics for Computer Science, Spring 2015](https://www.youtube.com/playlist?list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ) and also try to examine your understand through their quiz and exams from [Mathematics for Computer Science MIT OCW main site](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/).
  - [ ] Algebra Section 
  - [ ] [English translation of e-maxx awesome algorithm text tutorial](http://cp-algorithms.com/)
  
# Others 
## System Design 
System design questions are crucial questions that show you are more than just a coder. You need to be able to think big picture as an engineer. Where do certain services belong, what kind of servers do you need, how would you manage traffic, etc. All of these ideas show that you are able to design software, not just code what people tell you to code.
  - [Parking Lot System](https://youtu.be/DSGsa0pu8-k)
  - [Whats App](https://www.youtube.com/watch?v=vvhC64hQZMk)
  - [Uber design](https://youtu.be/umWABit-wbk)
  - [Instagram](https://www.youtube.com/watch?v=QmX2NPkJTKg)
  - [Tinder Service](https://www.youtube.com/watch?v=xQnIN9bW0og)

## Database 
### SQL
#### Problems 
  - [Trips and Users](https://leetcode.com/problems/trips-and-users/)
  - [Human Traffic of Stadium](https://leetcode.com/problems/human-traffic-of-stadium/)
  - [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/)
  - [Exchange Seats](https://leetcode.com/problems/exchange-seats/)
  - [Hackerrank The Report](https://www.hackerrank.com/challenges/the-report/problem)
  - [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/)
  - [Symmetric Pairs](https://www.hackerrank.com/challenges/symmetric-pairs/problem)
  - [OccupationsPlacements](https://www.hackerrank.com/challenges/occupations/problem)
  - [Ollivander's Inventory](https://www.hackerrank.com/challenges/harry-potter-and-wands/problem)
#### General
  - [SQL Query Interview Questions](https://www.youtube.com/watch?v=uAWWhEA57bE)
  - [Learning about ROW_NUMBER and Analytic Functions](https://www.youtube.com/watch?v=QFj-hZi8MKk)
  - [Advanced Implementation Of Analytic Functions](https://www.youtube.com/watch?v=G3kYPzLWtpo&t=4s)
  - [Advanced Implementation Of Analytic Functions Part 2](https://www.youtube.com/watch?v=XecU6Ieyu-4&t=54s)
  - [Wise Owl SQL Videos](https://www.youtube.com/watch?v=2-1XQHAgDsM&list=PL6EDEB03D20332309)

### Transaction

## Operating System
  - [Commonly Asked Operating Systems Interview Questions](https://www.geeksforgeeks.org/commonly-asked-operating-systems-interview-questions-set-1/)
  - [What is Translation lookaside buffer?](https://www.geeksforgeeks.org/operating-system-translation-lookaside-buffer-tlb/)
  - [Why does Round Robin avoid the Priority Inversion Problem?](https://leetcode.com/discuss/interview-question/operating-system/220604/Why-does-Round-Robin-avoid-the-Priority-Inversion-Problem)
  - [Interrupt Vs System Call---What is 'inode' in file system?](https://leetcode.com/discuss/interview-question/operating-system/124838/Interrupt-Vs-System-Call)
  - [Operating System Interview Questions and Answers --- Part I](https://www.youtube.com/watch?v=b18X4uOKjHs)
  - [What is a kernel --- Gary explains](https://www.youtube.com/watch?v=mycVSMyShk8)
  - [Round Robin Algorithm Tutorial (CPU Scheduling)](https://www.youtube.com/watch?v=aWlQYllBZDs)
  - [The Magic of LRU Cache (100 Days of Google Dev)](https://www.youtube.com/watch?v=R5ON3iwx78M)
  - [The Memory Hierarchy](https://www.youtube.com/watch?v=vjYF_fAZI5E&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-&index=24)
  - [Interrupts](https://www.youtube.com/watch?v=uFKi2-J-6II&list=PLCiOXwirraUCBE9i_ukL8_Kfg6XNv7Se8&index=3)
  - [Scheduling](https://www.youtube.com/watch?v=-Gu5mYdKbu4&index=4&list=PLCiOXwirraUCBE9i_ukL8_Kfg6XNv7Se8)

## Concurrency 
  - [User Level thread Vs Kernel Level thread](https://leetcode.com/discuss/interview-question/operating-system/124631/User-Level-thread-Vs-Kernel-Level-thread)
  - [Intro to Processes & Threads](https://www.youtube.com/watch?v=exbKr6fnoUw)
  - [Difference Between Process and Thread --- Georgia Tech --- Advanced Operating Systems](https://www.youtube.com/watch?v=O3EyzlZxx3g&t=11s)
  - [Difference between forking and multithreading](https://leetcode.com/discuss/interview-question/operating-system/125024/Difference-between-forking-and-multithreading)
  
## Cache 
  -  LRU cache:
 	- [The Magic of LRU Cache (100 Days of Google Dev)](https://www.youtube.com/watch?v=R5ON3iwx78M)
 	- [Implementing LRU ](https://www.youtube.com/watch?v=bq6N7Ym81iI)
 	- [LeetCode - 146 LRU Cache](https://www.youtube.com/watch?v=8-FZRAjR7qU)
  -  CPU cache:
 	- [MIT 6.004 L15: The Memory Hierarchy](https://www.youtube.com/watch?v=vjYF_fAZI5E&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82-&index=24)
 	- [MIT 6.004 L16: Cache Issues](https://www.youtube.com/watch?v=ajgC3-pyGlk&index=25&list=PLrRW1w6CGAcXbMtDFj205vALOGmiRc82)
	
## OOP 
  - [Inheritance](https://www.youtube.com/watch?v=9JpNY-XAseg)
  - [Introduction to Polymorphism](https://www.youtube.com/watch?v=0xw06loTm1k)
  - [Abstract and Concrete Classes](https://www.youtube.com/watch?v=TyPNvt6Zg8c)
  - [Overriding Rules](https://www.youtube.com/watch?v=zN9pKULyoj4&t=3s)
  - [Class to Hold Objects](https://www.youtube.com/watch?v=slY5Ag7IjM0)
  - [Object-Oriented Programming](https://www.youtube.com/watch?v=lbXsrHGhBAU)

## Design Patterns 
  - [Sources1](https://sourcemaking.com/design_patterns)
  - [Sources2](https://refactoring.guru/design-patterns)
  - [Factory Design Pattern](https://www.youtube.com/watch?v=ub0DXaeV6hA)
  - [Observer Design Pattern](https://youtu.be/wiQdrH2YpT4)
  - [Adapter Design Pattern](https://www.youtube.com/watch?v=qG286LQM6BU&list=PLF206E906175C7E07&index=13)
  - [Facade Design Pattern](https://www.youtube.com/watch?v=B1Y8fcYrz5o&list=PLF206E906175C7E07&index=14)
  - [Chain of Responsibility Design Pattern](https://www.youtube.com/watch?v=jDX6x8qmjbA&list=PLF206E906175C7E07&index=22)
  - [Interpreter Design Pattern](https://www.youtube.com/watch?v=6CVymSJQuJE&list=PLF206E906175C7E07&index=23)
  - [Singleton Design Pattern Tutorial](https://www.youtube.com/watch?v=NZaXM67fxbs&list=PLF206E906175C7E07&index=7)
  - [Patterns](https://youtu.be/LAP2A80Ajrg?list=PLJ9pm_Rc9HesnkwKlal_buSIHA-jTZMpO&t=3344)
  - [Head First Design Patterns](https://www.amazon.com/Head-First-Design-Patterns-Freeman/dp/0596007124)

## Conclusion 
```java 
While 1:
	print("Deliberate Strategic Practice")
	print("Study and implement New DSA")
	print("Simulate real environement and test yourself") # do contest, contest and contest
```
The secret is nothing but **Regular Deliberate Strategic Practice**. We always try to solve questions beyond our comfort zone and do it regularly. And that is it really. Always solve questions that we are not comfortable with, push yourself. Try to solve topic wise after we get a good general grasp of DSA. Find your weakness and work on it. Hard work will pay you off one day. Just want to finish with one of my favorite quote by Mark Manson:

""I wanted the reward and not the struggle. I wanted the result and not the process. I was in love not with the fight but only the victory. And life doesn't work that way.""

## Comprehensive gold materials 
  -  [Comprehensive Data Structure and Algorithm Study Guide](https://leetcode.com/discuss/general-discussion/494279/comprehensive-data-structure-and-algorithm-study-guide)
  -  [Coding Interview University by John Washam](https://github.com/jwasham/coding-interview-university)
  -  [Practice Python by John Washam](https://github.com/jwasham/practice-python)
  -  [CP and CI Study materials by Jasmine Chen(Google SWE)](https://github.com/lnishan/awesome-competitive-programming) : this one is gold
  -  [Great guideline on acing interviews and what to study?](https://medium.com/@nick.ciubotariu/ace-the-coding-interview-every-time-d169ce1fd3fc)
  -  [DSA for CP guys(CI guys should also try if you have time)](http://cp-algorithms.com/)
  -  [Crackign the interview](https://www.youtube.com/playlist?list=PLX6IKgS15Ue02WDPRCmYKuZicQHit9kFt)
