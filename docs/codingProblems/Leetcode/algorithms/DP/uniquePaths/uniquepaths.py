class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        # To compute the bottom left corner 
        dp[n-1][m] = 1 
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]