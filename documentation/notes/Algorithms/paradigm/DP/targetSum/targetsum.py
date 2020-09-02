from collections import defaultdict

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        MAX = sum(nums)
        N = len(nums)
        if (sum(nums) < S):return 0
        dp = [[0 for _ in range(MAX*2+1)] for _ in range(N + 1)]
        dp[0][MAX] = 1 
        for i in range(1,N+1):
            for r in range(MAX*2+1):
                remain = r-MAX
                temp = remain-nums[i-1]
                if temp >= -MAX:
                    dp[i][r] += dp[i-1][temp+MAX]
                temp = remain+nums[i-1]
                if temp <= MAX:
                    dp[i][r] += dp[i-1][temp+MAX]
        return dp[N][S+MAX]


# 代码优化+滚动数组降维
    def findTargetSumWays_1d(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        MAX = sum(nums); N = len(nums); OFFSET = MAX; kMaxN = MAX*2+1
        if (sum(nums) < S):return 0
        dp_prep = defaultdict(int)
        dp_prep[OFFSET] = 1 
        for n in nums:
            dp_cur = defaultdict(int)
            for r in range(n,kMaxN-n):
                if r in dp_prep:
                    dp_cur[r+n] += dp_prep[r]
                    dp_cur[r-n]  += dp_prep[r]
            dp_prep = dp_cur
        return dp_prep[S+OFFSET]

# 变形-> 0/1 knapsack problem 

    def findTargetSumWays_optimized(self,nums,S):
        S = abs(S)
        MAX = sum(nums)
        if (S>MAX or (S+MAX)%2 != 0): return 0
        target = (S+MAX) / 2
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for n in nums:
            for i in reversed(range(n,target+1)):
                dp[i] += dp[i - n]
        return dp[target]
                
if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1]
    S = -3 
    print("Output : {}".format(s.findTargetSumWays(nums,S)))