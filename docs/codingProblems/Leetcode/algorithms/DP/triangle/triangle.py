# triangle: https://leetcode.com/problems/triangle/

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        dp = [[ 0 for j in range(i+1)] for i in range(row+1)]
        for i in reversed(range(row)):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]
        
