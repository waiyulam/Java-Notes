#!/bin/python
# Minimum path sum : https://leetcode.com/problems/minimum-path-sum/ 

import sys 

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        DP = [[0]* n] * m
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if (i+1) == m and (j+1) == n:
                    DP[i][j] = grid[i][j]
                elif (i+1) == m:
                    DP[i][j] = grid[i][j] + DP[i][j+1]
                elif (j+1) == n:
                    DP[i][j] = grid[i][j] + DP[i+1][j]
                else:
                    DP[i][j] = grid[i][j] + min(DP[i][j+1],DP[i+1][j])
        return DP[0][0]



if __name__ == "__main__":
    s = Solution()
    grid = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
            ]
    print("Output: {}".format(s.minPathSum(grid)))
