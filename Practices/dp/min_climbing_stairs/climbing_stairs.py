#!/bin/python
# Leetcode: https://leetcode.com/problems/min-cost-climbing-stairs/

import sys 

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Subproblem: find the minimum cost to reach top of the floor starting at [i: ]
        # or find the minimum cost to reach [i: ] and the original problem is min(DP[n-1],DP[n-2])
        # The smallest subproblem is at the top of the floor 
        n = len(cost)
        DP = [0] * n
        DP[n-1] = 0
        DP[n-2] = 0
        for i in reversed(range(n-2)):
            DP[i] = min(DP[i+1] + cost[i+1],DP[i+2]+cost[i+2])
        
        # Original problem : DP[-1]
        return min(cost[0]+DP[0],cost[1]+DP[1])


if __name__ == "__main__":
    s = Solution()
    cost = [10, 15, 20]
    print("Output: {}".format(s.minCostClimbingStairs(cost)))
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print("Output: {}".format(s.minCostClimbingStairs(cost)))