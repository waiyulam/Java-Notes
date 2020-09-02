#!/bin/python
# Coin change : https://leetcode.com/problems/coin-change/
# Solutions : https://leetcode.com/articles/coin-change/ 

import sys 

# Bottom up solutions 
# F(S) - minimum number of coins needed to make change for amount S using coin denominations
class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [sys.maxsize] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin,amount+1):
                # dp[x] 
                dp[x] = min(dp[x],dp[x-coin] + 1)
        return dp[amount] if dp[amount] != sys.maxsize else -1

""" java  top down solution 
public class Solution {

  public int coinChange(int[] coins, int amount) {
    if (amount < 1) return 0;
    return coinChange(coins, amount, new int[amount]); // new int[amount]: memoization 
  }

  private int coinChange(int[] coins, int rem, int[] count) {
    // Base case 
    if (rem < 0) return -1;
    if (rem == 0) return 0;

    // Memoization : if the F(S) is repeated
    if (count[rem - 1] != 0) return count[rem - 1];

    // The rem is positive 
    // min keep the minimum value by traversing all possible selection of coins 
    int min = Integer.MAX_VALUE;

    for (int coin : coins) {
      int res = coinChange(coins, rem - coin, count);
      // res >= 0 : valid , if it is -1 then the selection is not valid to change total amount 
      // res < min : only keep the minimum value 

      if (res >= 0 && res < min)
        min = 1 + res;
    }

    // if min == maxvalue, then there is no valid selection of coin can be used. 
    count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
    return count[rem - 1];
  }
}
"""

if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    print("Output: {}".format(s.coinChange(coins,amount)))
    coins = [2]
    amount = 3
    print("Output: {}".format(s.coinChange(coins,amount)))
