class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        SUM = sum(nums)//2
        N = len(nums)
        # 减枝
        if (sum(nums)%2) != 0: return False 
        # 创建背包
        dp = [0 for _ in range(SUM+1)]
        # 初始值
        dp[0] = True

        for i in range(N):
            for j in reversed(range(nums[i],SUM+1)):
                dp[j] = dp[j-nums[i]] or dp[j]
        return dp[SUM]





