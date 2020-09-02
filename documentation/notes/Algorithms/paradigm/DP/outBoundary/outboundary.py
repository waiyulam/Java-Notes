class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        start_i  = i+1
        start_j  = j+1
        kmod = 1e9 + 7
        # 创建背包
        dp = [[[0 for _ in range(n+2)] for _ in range(m+2)] for _ in range(N+1)]
        # 初始背包(边界)
        for i in range(N+1):
            for j in range(n+2):
                dp[i][0][j] = 1
                dp[i][m+1][j] = 1
            for j in range(m+2):
                dp[i][j][0] = 1
                dp[i][j][n+1] = 1

        # bottom- up 递归
        for i in range(1,N+1):
            for j in range(1,m+1):
                for k in  range (1,n+1):
                    dp[i][j][k] = dp[i-1][j+1][k] + dp[i-1][j-1][k] + dp[i-1][j][k+1] + dp[i-1][j][k-1]
                    dp[i][j][k] %= kmod
        
        return dp[N][start_i][start_j] 
        

    def findPaths_reduced(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """   
        start_i  = i+1
        start_j  = j+1
        kmod = 1e9 + 7
        # 创建背包
        dp_prep = [[0 for _ in range(n+2)] for _ in range(m+2)]
        # 初始背包(边界)
        for j in range(n+2):
            dp_prep[0][j] = 1
            dp_prep[m+1][j] = 1
        for j in range(m+2):
            dp_prep[j][0] = 1
            dp_prep[j][n+1] = 1

        # bottom- up 递归
        for i in range(1,N+1):
            dp_cur = [[dp_prep[i][j] for j in range(n+2)] for i in range(m+2)]
            for j in range(1,m+1):
                for k in  range (1,n+1):
                    dp_cur[j][k] = dp_prep[j+1][k] + dp_prep[j-1][k] + dp_prep[j][k+1] + dp_prep[j][k-1]
                    dp_cur[j][k] %= kmod
            dp_prep = [[dp_cur[i][j] for j in range(n+2)] for i in range(m+2)]
        return dp_prep[start_i][start_j] 


if __name__ == "__main__":
    s = Solution()
    m = 2; n = 2; N = 2; i = 0; j = 0
    print("Output: {}".format(s.findPaths(m,n,N,i,j)))
