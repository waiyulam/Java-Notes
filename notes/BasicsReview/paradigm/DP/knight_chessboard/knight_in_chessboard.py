class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        TOTALMOVES = pow(8,K)
        dp = [[[0 for _ in range(N+4)] for _ in range(N+4)] for _ in range(K+1)]
        for i in range(2,N+2):
            for j in range(2,N+2):
                dp[0][i][j] = 1

        for k in range(1,K+1):
            for i in range(2,N+2):
                for j in range(2,N+2):
                    dp[k][i][j] = dp[k-1][i+2][j+1]+dp[k-1][i+2][j-1]+dp[k-1][i-2][j+1]+dp[k-1][i-2][j-1]
                    dp[k][i][j] += dp[k-1][i+1][j+2]+dp[k-1][i+1][j-2]+dp[k-1][i-1][j+2]+dp[k-1][i-1][j-2]
        return dp[K][r+2][c+2]/float(TOTALMOVES)
        

# 代码优化+滚动数组降维
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        TOTALMOVES = pow(8,K)
        dp_prep = [[0 for _ in range(N+4)] for _ in range(N+4)] 
        for i in range(2,N+2):
            for j in range(2,N+2):
                dp_prep[i][j] = 1

        for k in range(0,K):
            dp_cur = [[0 for _ in range(N+4)] for _ in range(N+4)] 
            for i in range(2,N+2):
                for j in range(2,N+2):
                    dp_cur[i][j] = dp_prep[i+2][j+1]+dp_prep[i+2][j-1]+dp_prep[i-2][j+1]+dp_prep[i-2][j-1]
                    dp_cur[i][j] += dp_prep[i+1][j+2]+dp_prep[i+1][j-2]+dp_prep[i-1][j+2]+dp_prep[i-1][j-2]
            dp_prep = dp_cur[:][:]
        return dp_prep[r+2][c+2]/float(TOTALMOVES)       

if __name__ == "__main__":
    s = Solution()
    N = 5;K=1;r=0;c=0
    print("Output : {}".format(s.knightProbability(N,K,r,c)))