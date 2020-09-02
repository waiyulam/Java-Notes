class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M = len(obstacleGrid) 
        if M == 0:
            return 0
        N = len(obstacleGrid[0])
        if N == 0:
            return 0
    
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        dp[M-1][N] = 1 
        for i in reversed(range(M)):
            for j in reversed(range(N)):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1] 
                
        return dp[0][0]


if __name__ == "__main__":
    s = Solution()
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print("Output: {}".format(s.uniquePathsWithObstacles(obstacleGrid)))