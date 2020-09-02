class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        KMOD = 1e10 + 7
        # 创建背包： 
        dp = [[0 for _ in range(2)] for _ in range(N+1)]
        dp[0][0] = dp[1][0] = 1 

        for i in range(2,N+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + dp[i-1][1]  + dp[i-1][2]
            dp[i][1] = dp[i-2][0] + dp[i-2][1] 
        
        return dp[N][0]