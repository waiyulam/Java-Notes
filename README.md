# Interview-Prep-Guide
Cracking the interview : Interviewing can be tough because you can feel like you are making no progress. Having this study guide will help you track your progress and give you a better read on how you are doing!    
Don't Rush. Enjoy the journey. Try to be a natural problem solver not a interview acing problem solver. And you are not alone!  
**Keep moving mate, never ever dare to give up. Hard work is going to pay you off very soon.**

![](https://media.giphy.com/media/KWQy384u0Rn9bCvwMa/giphy.gif)

# CS Fundamentals 
## Introduction to Algorithms 
### Time & Space Complexity 
  -  [Video no. 1-16 Abdul Bari's Algorithm Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)  
ps:After watching this 16 videos i can guarantee that you will gain mastery on Time Complexity for sure.)  

  -  [A Gentle Introduction to Algorithm Complexity Analysis](http://discrete.gr/complexity/)
  -  [Cheat Sheet](http://bigocheatsheet.com/)
  
### Programming Paradigm (Review ECS122A)
#### - Recursion and analysis of recurrence relations
  -  [Recursion Playlist by mycodeschool](https://www.youtube.com/playlist?list=PL2_aWCzGMAwLz3g66WrxFGSXvSsvyfzCO)
  -  [Masters Theorem for the proof of recursion](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)
video no. 18 to no. 29 from Abdul Bari's Algorithm Playlist 
  -  [Sparknotes tutorial on recursion types](https://www.sparknotes.com/cs/recursion/whatisrecursion/section2/)
  -  Chapter 4 | Divide and Conquer | Page No.65 from Introduction to Algorithm by CLRS
  -  UC Davis ECS122A 

Almost everyone knows what recursion is, right? But that is not enough. You have to create some sort of mental model how recursion actually saves states by pushing function code to stack and reaches at the last/smallest problem and then solves it and then backtrack from there by poping function code from stack to top and etc. You have to spend sufficient time to understand recursion through studying and practicing, as recursion is will be the base of everything in this type.

#### - Divide and Conquer algorithms 
  -  Implement merge sort, segment tree, binary search etc. And study [Video no. 18, 33 to 38 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)

#### - Greedy Algorithms:  Huffman Coding
  -  Proofing greedy algorithm is quite difficult. Studying known problems like knapsack, job schedule, optimal merge pattern, Huffman coding etc are enough to ace greedy questions. Study [Video no.39-no.45 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)
  
#### - Backtracking & Branch and Bound
  -  Study [Video no.63 to no.71 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O). This topic is the key ingredient to solve Dynamic Programming questions.

#### - Big Guy: Dynamic Programming and memoization 😭
Recognize the pattern/formula for a dp problem. Say for example: A String based DP problem involves a 2D matrix where [i][j] generally refers to the solution for index i to j of the String and etc. Here is what you should do, try to understand backtracking very well as that will be the key in solving DP. After getting a backtracking solution you can memoize the previous solutions and reduce solutions to 2/3 Degree Polynomial Time. 

  -  [Intro](https://www.youtube.com/watch?v=iv_yHjmkv4I)
  - [video no.19(MUST MUST!),20-22,26-27,39-45 from MIT OCW Introduction to Algorithm](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
  -  [DP & Memoization](https://www.youtube.com/watch?v=P8Xa2BitN3I&t=13s)

Anyway, you have to study known DP problems as much as you possibly can and try to recognize the patterns and types. 
  -  [Fibonacci, Shortest Paths](https://www.youtube.com/watch?v=OQ5jsbhAv_M&t=7s) : Dijkstron & Floyd Warshall
  -  [Text Justification, Blackjac](https://www.youtube.com/watch?v=ENyox7kNKeY&t=4s)
  -  [Leetcode Coin(giveaway) winning post on Dynamic Programming Patterns by aatalyk](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
  -  [Tushar Roy's Dynamic Programing Playlist](https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr)
  -  [Video no.46 to no.60 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)
  -  [Cheat Sheet](https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/)
  
**Comment**: I find **Abdul bari's tutorial** more effective and easy to follow. His style to teach students is quite exceptional. Suppose you are studying Longest Common Subsequence, first understand the question really good -> try to solve a small problem of the main problem -> try to solve a bit big problem with the help of solution and see if you can find any formula/pattern -> if you can't find any then read discussion/solution(only algorithm not code) and try to code it up after understanding -> If still doesn't work for you then watch the video of that topic from the playlist i have mentioned and try hard this time to understand and visualize the algorithm. -> You solved a DP Question!   

**Tips**: **Pythonistas** After you just come up with a 2N backtracking solution just use functools.lru_cache(maxsize=None) decorator and you will have a dp solution(almost 90% time).

#### - Graph Theory (directed, undirected, weighted, rooted(IN & OUT) and unrooted tree, DAG etc)
[Graph Theory Easy to Advanced Course - Full Tutorial from a Google Engineer and ACM ICPC World Finalist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P)

Comment: There are so much overlaps in between greedy, dp with graph theory. Say for example Dijkstra, Prim's and Kruskal's Minimum Spanning tree are just Greedy Algorithms or backtracking is just DFS with branch pruning with condition. So you will find it a lot easier after studying programming paradigm section. In fact graph problems are either so easy to recognize that everything is given so explicitly that any one can recognize it as a typical graph question or may be it's too hidden to even think it as a graph question. So my suggestion is to think out of the box for a problem, think if a problem can be solved by using graphs. **Never forget that, Interviewers are just obsessed with binary tree, so try to solve as many questions as you can related to tree, specifically binary tree(and also n-ary tree). And also solve at least 20 questions with tag BFS and DFS in Leetcode which will definitely boost your tree and graph problem solving skill as graph traversal is the main toolkit to solve tree/graph problems in interview. That's all about graph.** 

#### - Mathmatics (Number theory, Computational Geometry, Combinatorics, Linear Algebra etc)
  - [MIT 6.042J Mathematics for Computer Science, Spring 2015](https://www.youtube.com/playlist?list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ) and also try to examine your understand through their quiz and exams from [Mathematics for Computer Science MIT OCW main site](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-spring-2015/).
  - Algebra Section 
  - [English translation of e-maxx awesome algorithm text tutorial](http://cp-algorithms.com/)

#### - NP-completenes

#### - String Manipulation 
  -  Follow the string section from [CP Algorithms Site](http://cp-algorithms.com/).
  -  [Longest Consecutive Characters](https://www.youtube.com/watch?v=qRNB8CV3_LU)
  -  [Substring Search](https://www.coursera.org/learn/algorithms-part2/home/week/4)
  -  Linear-time string matching: Z algorithm 

#### - Bit Manipulation 
  -  Follow [HackerEarth Bit Manipulation Tutorial](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/) and also [TopCoder Fun with Bits Tutorial](https://www.topcoder.com/community/competitive-programming/tutorials/a-bit-of-fun-fun-with-bits/).

## Data Structures
![](https://res.cloudinary.com/practicaldev/image/fetch/s--WlnYH5fq--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn-images-1.medium.com/max/1600/1%2ADyu63sMUVL-gYEZISOE2BQ.jpeg)

[Data Structures Easy to Advanced Course - Full Tutorial from a Google Engineer and ACM ICPC World Finalist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu)  

ps:This is one of the best materials to study on data structure topic. William implemented each on Java. But it doesn't really matter which language you use, i did this course in both in c++ and python. And try to code yourself after watching a data structure topic and do some leetcode question on that. And this is all you need to ace DS questions.)

### Arrays 
  - [Multi-dim Array](https://archive.org/details/0102WhatYouShouldKnow/02_05-multidimensionalArrays.mp4) 
  - [Dynamic Array](https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV)
  - [Resizing Array](https://archive.org/details/0102WhatYouShouldKnow/03_01-resizableArrays.mp4)

### Linked Lists
  -  [Intro](https://www.youtube.com/watch?v=njTh_OwMljA&feature=youtu.be) 
  -  [Linked Lists vs Array](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9)

### Trees
  -  [Intro](https://www.youtube.com/watch?v=oSWTXtMglKE&feature=youtu.be)

### Heaps
  -  [Intro](https://www.youtube.com/watch?v=t0Cq6tVNRBA&feature=youtu.be)

### Hash Table
  -  [Intro](https://www.youtube.com/watch?v=shs0KM3wKv8&feature=youtu.be)
  -  [Phone Book Problem](https://www.coursera.org/learn/data-structures/lecture/NYZZP/phone-book-problem)

### Stacks and Queues
  -  [Intro](https://youtu.be/wjI1WNcIntg)
  -  [Using Stacks Last-In First-Out ](https://archive.org/details/0102WhatYouShouldKnow/05_01-usingStacksForLast-inFirst-out.mp4)

### Tries
  -  [Intro](https://www.youtube.com/watch?v=zIjfhVPRZCg)

### Others 
  -  [Data Structure Intro](https://www.youtube.com/watch?v=bum_19loj9A)
  -  [Crash Course Computer Science](https://www.youtube.com/watch?v=DuDz6B4cqVc&feature=youtu.be)


## Algorithms 
![](https://res.cloudinary.com/practicaldev/image/fetch/s--POn2iYyz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://cdn-images-1.medium.com/max/1600/1%2AbPpvELo9_QqQsDz7CSbwXQ.gif) 

### Graph Search 
  -  [Intro](https://www.youtube.com/watch?v=zaBhtODEL0w&list=PLX6IKgS15Ue02WDPRCmYKuZicQHit9kFt)
  -  [BFS(breadth-first search) and DFS(depth-first search)](https://www.youtube.com/watch?v=uWL6FJhq5fM)

### Binary Search 
  -  [Intro](https://youtu.be/P3YID7liBug)
  -  [Binary Search Tree Review](https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
  
### Sorting
  -  [Bubble Sort](https://youtu.be/6Gv8vg0kcHc)
  -  [Merge Sort](https://youtu.be/KF2j-9iSf4Q)
  -  [Quick Sort](https://youtu.be/SLauY6PpjW4)
  
## Best DSA study Link
  -  [TopCoder Competitive Programming Tutorials](https://www.topcoder.com/community/competitive-programming/tutorials/)
  -  [Technical interview Guide by Yangshun](https://yangshun.github.io/tech-interview-handbook/introduction/)
  -  [HackerEarth CodeMonk(step by step Guide)](https://www.hackerearth.com/practice/codemonk/)
  -  [Python Algorithms for Interviews](https://www.youtube.com/watch?v=p65AHm9MX80)

# Run practice problems

## [hackerrank](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/hackerrank)
- [Implementation Category of hackerrank](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=implementation&badge_type=problem-solving)

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
  -  [CP and CI Study materials by Jasmine Chen(Google SWE)](https://github.com/lnishan/awesome-competitive-programming) : this one is gold
  -  [Great guideline on acing interviews and what to study?](https://medium.com/@nick.ciubotariu/ace-the-coding-interview-every-time-d169ce1fd3fc)
  -  [DSA for CP guys(CI guys should also try if you have time)](http://cp-algorithms.com/)
  -  [Crackign the interview](https://www.youtube.com/playlist?list=PLX6IKgS15Ue02WDPRCmYKuZicQHit9kFt)
