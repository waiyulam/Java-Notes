from collections import defaultdict

class Solution(object):
    # Time exceed 
    def findNumberOfLIS_Exceed(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        # 创建背包
        dp = [[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            dp[i][0] = 1

        # 递归
        MAX = 0
        for i in range(1,N):
            for j in range(1,i+1):
                for k in range(i):
                    if nums[k] < nums[i]:
                        dp[i][j] += dp[k][j-1]
                if dp[i][j] != 0:
                    MAX = max(MAX,j)

        ans = 0 

        for i in range(N): 
            ans += dp[i][MAX]
        return ans
    
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        # 创建背包: 
        # length[i] = longest ending in nums[i]
        length = [0 for i in range(N)]
        # count[i] = number of longest ending in nums[i]
        counts = [1 for i in range(N)]    
        for i in range(1,N):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j] +1:
                        counts[i] += counts[j]
                    elif length[i] <= length[j]:
                        length[i] = length[j] +1
                        counts[i] = counts[j]
        MAX_length = max(length)
        return sum(c for i, c in enumerate(counts) if length[i] == MAX_length)

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,4,7]
    print("Output: {}".format(s.findNumberOfLIS(nums)))


