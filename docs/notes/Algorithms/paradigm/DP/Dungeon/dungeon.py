import sys
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if dungeon is None:
            return 1
        # dungeon has size m*n 
        m = len(dungeon); n = len(dungeon[0])
        # # Initialize cache
        dp = [[sys.maxsize for i in range(n+1)] for j in range(m+1)]
        dp[m][n-1] = dp[m-1][n-1] = 1
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                # 首先在这一格Knight至少要多少health 
                dp[i][j] = max(1,min(dp[i+1][j],dp[i][j+1]) - dungeon[i][j])
        
        return dp[0][0]
        
    def calculateMinimumHP_dp_noHelper(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if dungeon is None:
            return 1
        # dungeon has size m*n 
        m = len(dungeon); n = len(dungeon[0])
        # # Initialize cache
        # dp = [[sys.maxsize for i in range(n+1)] for j in range(m+1)]
        # No need dp to reduce space complexity as we overwrite value on dungeon

        # Bounding case 
        # bottom corner : 
        dungeon[m-1][n-1] = max(-dungeon[m-1][n-1],0) + 1

        for i in reversed(range(n-1)):
            dungeon[m-1][i] = max(1, dungeon[m-1][i+1] - dungeon[m-1][i])

        for i in reversed(range(m-1)):
            dungeon[i][n-1] = max(1, dungeon[i+1][n-1] - dungeon[i][n-1])


        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                # 首先在这一格Knight至少要多少health 
                dungeon[i][j] = max(1,min(dungeon[i+1][j],dungeon[i][j+1]) - dungeon[i][j])
        
        return dungeon[0][0]





if __name__ == "__main__":
    s = Solution()
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print("Mininum health :  {}".format(s.calculateMinimumHP(dungeon)))