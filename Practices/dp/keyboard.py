# 2 key keyboard : https://leetcode.com/problems/2-keys-keyboard/

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i] denote minimal operations for i 'A'
        dp = [[sys.maxsize] for i in range(n+1)]
        # A
        dp[1] = 0
        # AA 
        dp[2] = 2
        for i in range(3,n+1):
            for j in range(1,i):
                # copy from anywhere when the number of missing 'A' (i-j)
                # is dividable by the number of existing 'A' (j)
                # the bottom line is when j == 1
                # 1 copy + (i-j)/j paste
                if ((i-j)%j == 0):
                    dp[i] = min(dp[i],dp[j] + 1+ (i-j)//j)
        return dp[n]
        