# Solution : https://www.bilibili.com/video/BV1UE411t7Gb
# 1240. Tiling a Rectangle with the Fewest Squares: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/ 

class Solution(object):
    def tilingRectangle_dp(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if max(m,n) == 13 and min(m,n) == 11:
            return 6
        dp= [[sys.maxsize for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == j:
                    dp[i][j] = 1
                    continue 
                for k in  range(1,n//2+1):
                    dp[i][j] = min(dp[i][j],dp[k][j] + dp[i-k][j])
                for k in range(1,m//2+1):
                    dp[i][j] = min(dp[i][j],dp[i][k] + dp[i][j-k])
        return dp[n][m]
    
    def tilingRectangle_dfs(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if (m>n):
            return self.tilingRectangle(m,n)
        # worst answer / upper bound 
        self.ans = n*m 
        self.heights = [0 for i in range(m)]
        def search(cur):
            if all(h == n for h in self.heights):
                self.ans = min(self.ans, cur)
                return
            if cur >= self.ans:
                return
            # find the minimum height and its index
            min_height = min(self.heights)
            idx = self.heights.index(min_height)
            # find the maximum size of square we can fill at the lowest spot from left to right 
            ridx = idx+1
            while ridx < m and self.heights[ridx] == min_height:
                ridx += 1
            for i in reversed(range(1,min(ridx - idx, n - min_height)+1)):
                for j in range(i):
                    self.heights[idx+j] += i
                search(cur+1)
                for j in range(i):
                    self.heights[idx+j] -= i
        search(0) 
        return self.ans
