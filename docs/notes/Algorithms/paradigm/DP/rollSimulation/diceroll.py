from collections import defaultdict
class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        MOD= pow(10,9) + 7
        # number of possible numbers for each roll 
        FACES = 6
        # MAXIMUM CONSTRAINT
        MAX = 15
        # 创建背包
        dp = [[[0 for _ in  range(rollMax[j]+1)] for j in range(FACES)] for _ in range(n+1)]
        # 初始化边界： i =0 
        for i in range(FACES):
            for j in range(1,rollMax[i]+1):
                dp[0][i][j] = 1

        # BOTTOM-UP 递归
        for i in range(1,n+1):
            for j in range(FACES):
                for k in range(1,rollMax[j]+1):
                    for p in range(FACES):
                        if j == p:
                            dp[i][j][k] += dp[i-1][p][k-1]
                        else:
                            dp[i][j][k] += dp[i-1][p][rollMax[p]]

        # Sum 
        ans = 0
        for i in range(FACES):
            ans += dp[n-1][i][rollMax[i]]

        return ans % MOD


if __name__ == "__main__":
    s = Solution()
    rollMax = [1,1,1,2,2,3]
    n = 3
    print("Output: {}".format(s.dieSimulator(n,rollMax)))
        

