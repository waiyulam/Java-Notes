import math
class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        # 1 serving == 25 ml
        N = int(math.ceil(N/25.0))
        #  When N is very large, this almost always happens (better than 99.9999%, so we can output 1)
        if N >= 200: return 1 
        # 创建背包
        dp = [[1.0 for _ in range(N+1)] for _ in range(N+1)]
        dp[0][0] = 0.5
        for i in range(1,N+1):
            dp[i][0] = 0.0

        for i in range(1,N+1):
            for j in range(1,N+1):
                dp[i][j] = 0.25*(dp[max(0,i-4)][j] + dp[max(0,i-3)][max(0,j-1)] + dp[max(i-2,0)][max(0,j-2)]+dp[max(0,i-1)][max(0,j-3)])

        return dp[N][N]
        
if __name__ == "__main__":
    s =Solution()
    N = 1
    print("Output: {}".format(s.soupServings(N)))