# Improving coin change bottom up dp algorithm
# perfect square: https://leetcode.com/problems/perfect-squares/ 
# Solution : https://www.cnblogs.com/grandyang/p/4800552.html
import sys 

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return 1
        dp = [sys.maxsize for i in range(0,n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            p = 1
            while pow(p,2) <= i:
                dp[i] = min(dp[i], dp[i-pow(p,2)] + 1)
                p += 1
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    n = 13
    print("output : {}".format(s.numSquares(n)))
