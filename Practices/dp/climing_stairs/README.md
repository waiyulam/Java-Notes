70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1**:

Input: 2   
Output: 2    
Explanation: There are two ways to climb to the top.    
1. 1 step + 1 step   
2. 2 steps   

**Example 2**:

Input: 3    
Output: 3    
Explanation: There are three ways to climb to the top.    
1. 1 step + 1 step + 1 step   
2. 1 step + 2 steps   
3. 2 steps + 1 step   
   

**Constraints**: 1 <= n <= 45


## DP solution 
Algorithm : As we can see this problem can be broken into subproblems, and it contains the optimal substructure property i.e. its optimal solution can be constructed efficiently from optimal solutions of its subproblems, we can use dynamic programming to solve this problem.   

One can reach ith step in two ways : 

1. Taking a single step from (i-1)th step 

2. Taking a step of 2 from (i-2)th step 

So, the total number of ways to reach ith is equal to sum of ways of reaching i-1)th step and ways of reaching (i-2)th step 

Let dp[i] denotes the number of ways to reach on ith step : 
```python
dp[i]=dp[i-1]+dp[i-2]
```

**Complexity Analysis**

Time complexity : O(n) 

Space complexity : O(n)
