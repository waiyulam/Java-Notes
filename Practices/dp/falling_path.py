#!/bin/python 
# Minimum Falling path sum : https://leetcode.com/problems/minimum-falling-path-sum/
# Solution : https://leetcode.com/problems/minimum-falling-path-sum/solution/ 
"""
This problem has an optimal substructure, meaning that the solutions to
subproblems can be used to solve larger instances of this problem. This makes
dynamic programming an ideal candidate.

Let dp(r, c) be the minimum total weight of a falling path starting at (r, c) and reaching the bottom row.

Then, dp(r, c) = A[r][c] + min(dp(r+1, c-1), dp(r+1, c), dp(r+1, c+1))
"""
import sys
class Solution(object):
   
    # Top down : Optimal sub problem : F(i,j) find the minimum falling path starting at (i,j) in A 
    # def minFallingPathSumUtil(self,i,j,A,count):
    #     # base case 
    #     if i == (len(A)-1):
    #         count[(i,j)]= A[i][j]
    #         return A[i][j]
        
    #     # Memoization 
    #     if (i,j) in count :
    #         return count[(i,j)]
        
    #     # Inductive step 
    #     minimum = sys.maxsize
    #     if (j!= 0):
    #         temp = self.minFallingPathSumUtil(i+1,j-1,A,count)
    #         if (temp < minimum):
    #             minimum = temp 
        
    #     if (j!= (len(A)-1)):
    #         temp = self.minFallingPathSumUtil(i+1,j+1,A,count)
    #         if (temp < minimum):
    #             minimum = temp 
        
    #     temp = self.minFallingPathSumUtil(i+1,j,A,count)
    #     if (temp < minimum):
    #         minimum = temp 

    #     count[(i,j)] = minimum + A[i][j]
    #     return count[(i,j)]

    # def minFallingPathSum(self, A):
    #     # :type A: List[List[int]]
    #     # :rtype: int
    #     n = len(A)
    #     minimum = sys.maxsize
    #     i = 0
    #     count = dict()
    #     for j in range(n):
    #         res = self.minFallingPathSumUtil(0,j,A,count)
    #         if count[(i,j)] < minimum:
    #             minimum = count[(i,j)]
    #     return minimum


    # Bottom up 
    def minFallingPathSum(self,A):
        dp = [[[0] for i in range(len(A))] for j in range(len(A))]
        for j in range(len(A)):
            dp[len(A)-1][j] = A[len(A)-1][j]
        for i in reversed(range(len(A)-1)):
            for j in range(len(A)):
                res = []
                res.append(dp[i+1][j])
                if j != 0:
                    res.append(dp[i+1][j-1])
                if j != len(A)-1:
                    res.append(dp[i+1][j+1])
                dp[i][j] = A[i][j] + min(res)
        return min(dp[0])

        

   
if __name__ == "__main__":
    s = Solution()
    A = [[51,24],[-50,82]]
    print("output: {}".format(s.minFallingPathSum(A)))
    A= [[69]]
    print("output: {}".format(s.minFallingPathSum(A)))