#!/bin/python 
# Minimum cost for tickets : https://leetcode.com/problems/minimum-cost-for-tickets/ 
# Solution : https://leetcode.com/problems/minimum-cost-for-tickets/solution/ 
import sys

"""
We can express those choices as a recursion and use dynamic programming. Let's
say dp(i) is the cost to fulfill your travel plan from day i to the end of the
plan. Then, if you have to travel today, your cost is:
dp(i)=min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])
"""

class Solution(object):
    # Window Variant
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # Bottom up 
        n = len(days)
        durations = [1,7,30]
        dp = [[0] for i in range(n+1)]
        dp[n] = 0

        for i in reversed(range(n)):
            minimum = sys.maxsize
            j = i 
            for c,d in zip(costs,durations):
                covered = days[i] + d - 1
                # Find the first index greater than covered day in days from day[i]
                while j < n and days[j] <= covered:
                    j += 1
                # Compute the cost 
                minimum = min(minimum,c + dp[j])
            dp[i] = minimum
        return dp[0]

""" Days variant 
class Solution(object):
    def mincostTickets(self, days, costs):
        # :type days: List[int]
        # :type costs: List[int]
        # :rtype: int
        N = days[-1]+1
        dp = [0]*N
        j = 0
        for i in range(1,N):
            if i == days[j]:
                dp[i] = min(dp[i-1]+costs[0], dp[max(0, i-7)]+costs[1], dp[max(0, i-30)]+costs[2])
                j += 1
            else:
                dp[i] = dp[i-1]
        return dp[-1]
"""      

if __name__ == "__main__":
    s = Solution()
    days = [1,4,6,7,8,20]
    costs = [7,2,15]
    print("output: {}".format(s.mincostTickets(days,costs)))
