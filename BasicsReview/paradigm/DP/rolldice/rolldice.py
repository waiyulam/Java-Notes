class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if target < d or target > d*f:
            return 0
        dp = [[0 for i in range(target+1)] for j in range(d+1)]
        dp[0][0] = 1
        for i in range(1,d+1):
            for j in range(i,min(target,i*f)+1):
                for k in range(1,min(j,f)+1):
                    dp[i][j] += dp[i-1][j-k]
                    
        return dp[d][target]%(10**9+7)

    def numRollsToTarget_1d(self,d,f,target):
        if target < d or target > d*f:
            return 0
        dp = [0 for i in range(target+1)]; mod = 10**9+7
        dp[0] = 1 
        for i in range(1,d+1):
            for t in range(min(target,i*f),min(i-1,target),-1):
                dp[t] = sum(dp[max(i-1,t-f):t]) % mod

        return dp[target]

if __name__ == "__main__":
    s = Solution()
    d = 3 
    f = 3
    target = 9 
    print("Output : {}".format(s.numRollsToTarget(d,f,target)))