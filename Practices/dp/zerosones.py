class Solution(object):
    def findMaxForm_DP(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # Brute force : 2^n for each element we have two choice 0 or 1 
        size = len(strs)
        dp = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(size+1)]
        for i in range(1,size+1):
            ones = strs[i-1].count('1')
            zeros = strs[i-1].count('0')
            for j in range(m+1):
                for k in range(n+1):
                    if j < zeros or k < ones:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k],dp[i-1][j-zeros][k-ones] + 1)
                        
        return dp[size][m][n]

# Reduce Space complexity 
    def findMaxForm(self,strs,m,n):
        # Brute force : 2^n for each element we have two choice 0 or 1 
        size = len(strs)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for s in strs:
            ones = s.count('1')
            zeros = s.count('0')
            for i in reversed(range(0,m+1)):
                for j in reversed(range(0,n+1)):
                    if i < zeros or j < ones:
                        dp[i][j] = dp[i][j]
                    else:
                        dp[i][j] = max(dp[i][j],dp[i-zeros][j-ones] + 1)
                        
        
        return dp[m][n]

if __name__ == "__main__":
    s = Solution()
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    print("Output: {}".format(s.findMaxForm(strs,m,n)))

