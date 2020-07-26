# Algorithms 

## Table of Contents 
- [Introduction to Algorithms](#Introduction-to-Algorithms)
    + [Time&Space Complexity](#Time-and-Space-Complexity)
    + [Recursion](#Recursion-and-analysis-of-recurrence-relations)
    + [NP program](#NP-program)
- [Searching](search)
- [Sorting](sorting)
- [Graph Theory](graphtheory)
- [String Manipulation](stringManipulation)
- [Bit Manipulation](bitManipulation)

## Introduction to Algorithms 
### Time and Space Complexity   
  -  [x] [Video no. 1-16 Abdul Bari's Algorithm Playlist](https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O)  
ps:After watching this 16 videos i can guarantee that you will gain mastery on Time Complexity for sure.)  

  -  [ ] [Overall Recall of Algorithm Complexity Analysis](http://discrete.gr/complexity/)
  -  [ ] [Cheat Sheet](http://bigocheatsheet.com/)
  
--- 
### Recursion and analysis of recurrence relations
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

--- 
### NP program
NP, NP-Complete and Approximation Algorithms
  -  [ ] Know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem, and be able to recognize them when an interviewer asks you them in disguise.
  -  [ ] [video no.23 from MIT OCW Introduction to Algorithm](https://www.youtube.com/watch?v=moPtwq_cVH8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=23)
  -  [ ] [Video no.72 to no.73 from Abdul Bari Algorithm's Playlist](https://www.youtube.com/watch?v=e2cF8a5aAhE&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=72)
  -  [ ] [Introduction to NP-Completeness](https://youtu.be/qcGnJ47Smlo?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=2939)
  -  [ ] [Approximate Greedy Algorithms for NP Complete Problems](https://www.geeksforgeeks.org/greedy-algorithms/#approximateGreedyAlgorthms)


