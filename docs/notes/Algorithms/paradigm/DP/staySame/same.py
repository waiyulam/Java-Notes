class Solution(object):
    def numWays_exceed(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        if arrLen == 1:
            return 1
        kmod = int(1e9 + 7)
        # 创建背包
        dp = [[0 for _ in range(arrLen+2)] for _ in range(steps+1)]
        # 初始背包： steps = 0 , index= 0 时只有一种方法
        dp[0][1] = 1 

        # bottom-up 
        for i in range(1,steps+1):
            for j in range(1,arrLen+1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]
                dp[i][j] %= kmod
        return dp[steps][1]

    # reduced and 降维
    def numWays(self, steps, arrLen):
        if arrLen == 1:
            return 1
        kmod = int(1e9 + 7)
        # 创建背包
        maxLength = min(steps//2+1,arrLen)
        dp_prep = [0 for _ in range(maxLength+2)] 
        # 初始背包： steps = 0 , index= 0 时只有一种方法
        dp_prep[1] = 1 
        # bottom-up 
        for i in range(1,steps+1):
            dp_cur = [0 for _ in range(maxLength+2)] 
            for j in range(1,maxLength+1):
                dp_cur[j] = dp_prep[j] + dp_prep[j-1] + dp_prep[j+1]
                dp_cur[j] %= kmod
            dp_prep = [dp_cur[j] for j in range(maxLength+2)]
        return dp_prep[1]


if __name__ == "__main__":
    s = Solution()
    steps = 430; arrLen = 148488          
    print("Output: {}".format(s.numWays(steps,arrLen)))
        