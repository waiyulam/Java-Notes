#last stone weight : https://leetcode.com/problems/last-stone-weight-ii/
# Dp hint : https://leetcode.com/problems/last-stone-weight-ii/discuss/672906/Explanation%3A-Why-Problem-is-Knapsack 
# DP explanation  : https://leetcode.com/problems/last-stone-weight-ii/discuss/653550/Trying-to-Explain-A-bit-(logic-behind-trick) 

"""
//let say array be [a,b,c,d]
//answer = (a+b)-(c+d) OR
//answer = a-(b+c+d) Or
//answer = (d+b)-(a+c) and so on.. any combination could be possible
//notice that in general I can say that
//answer = S1-S2
//where S1 is sum of some of the numbers and S2 is sum of rest of numbers
//also note that S1+S2 = SUM (sum of all numbers)
//S1 >= S2 beacuse negative answer is not possible
//now we have to minimise answer
//answer = SUM - 2*S2 (Just substituting S1 by SUM-S2)
//To minimise answer S2 has to be maximum
//Now, max value of S2 is SUM/2 (bigger than this and answer would be negative which is not possible)
//so the question reduces to find closest sum (sum of numbers) to (SUM/2)
//now this could be understood as subset sum problem or 0/1 knapsack problem
"""

import sys 


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        S = sum(stones)
        k = S // 2 
        n = len(stones)
        dp = [[0 for i in range(k+1)] for j in range(n+1) ]
        for i in range(1,n+1):
            for j in range(1,k+1):
                if stones[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-stones[i-1]]+stones[i-1])
        return (S - 2*dp[n][k])



if __name__ == "__main__":
    s = Solution()
    stones = [2]
    print("Output : {}".format(s.lastStoneWeightII(stones)))