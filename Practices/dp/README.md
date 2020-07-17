# Dynamic Programming Patterns

## Patterns
- [Minimum (Maximum) Path to Reach a Target](#Minimum(Maximum)-Path)
- [Distinct Ways](#Distinct-Ways)
- [Merging Intervals](#Merging-Intervals)
- [DP on Strings](#DP-on-Strings)
- [Decision Making](#Decision-Making)

### Minimum(Maximum) Path
Generate problem statement for this pattern    

**Statement** : Given a target find minimum (maximum) cost / path / sum to reach the target.  

**Approach** : Choose minimum (maximum) path among all possible paths before the current state, then add value for the current state.
```python
routes[i] = min(routes[i-1], routes[i-2], ... , routes[i-k]) + cost[i]
```

**Bottom up: Iterative solution**:Generate optimal solutions for all values in the target and return the value for the target.
```python
for (int i = 1; i <= target; ++i) {
   for (int j = 0; j < ways.size(); ++j) {
       if (ways[j] <= i) {
           dp[i] = min(dp[i], dp[i - ways[j]] + cost / path / sum) ;
       }
   }
}
return dp[target]
```
**Leetcode similar problems**:   
- [Min Cost Climbing Stairs](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/climbing_stairs)
- [Minimum Path Sum](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/mps)
- [**Coin Change**](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/coin_change)
- [Minimum Falling Path Sum](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/falling_path)
- [Minimum Cost For Tickets](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/cost_tickets)
- [2 Keys Keyboard](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/keyboard)
- [Perfect Squares](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/perfect_square)
- [**Last Stone Weight II**](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/stone2)
- [Triangle](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/triangle)
- [Ones and Zeroes](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/zerosones)
- [**Maximal Square**](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/maxsquare)
- [**Tiling a Rectangle with the Fewest Squares**](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/tilingrectangle)
- [**Dungeon Game**](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/Dungeon)
- [**Minimum Number of Refueling Stops**](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/refuelStop)

### Distinct Ways
**Statement** :Given a target find a number of distinct ways to reach the target.

**Approach** : Sum all possible ways to reach the current state.
```python
routes[i] = routes[i-1] + routes[i-2], ... , + routes[i-k]
```
Generate sum for all values in the target and return the value for the target.
```
for (int i = 1; i <= target; ++i) {
   for (int j = 0; j < ways.size(); ++j) {
       if (ways[j] <= i) {
           dp[i] += dp[i - ways[j]];
       }
   }
}
return dp[target]
```
70. Climbing Stairs easy
```python
for (int stair = 2; stair <= n; ++stair) {
   for (int step = 1; step <= 2; ++step) {
       dp[stair] += dp[stair-step];   
   }
}
```
62. Unique Paths Medium
```python
for (int i = 1; i < m; ++i) {
   for (int j = 1; j < n; ++j) {
       dp[i][j] = dp[i][j-1] + dp[i-1][j];
   }
}
```
1155. Number of Dice Rolls With Target Sum Medium
```python
for (int rep = 1; rep <= d; ++rep) {
   vector<int> new_ways(target+1);
   for (int already = 0; already <= target; ++already) {
       for (int pipe = 1; pipe <= f; ++pipe) {
           if (already - pipe >= 0) {
               new_ways[already] += ways[already - pipe];
               new_ways[already] %= mod;
           }
       }
   }
   ways = new_ways;
}
```

Note : Some questions point out the number of repetitions, in that case, add one more loop to simulate every repetition.

688. Knight Probability in Chessboard Medium

494. Target Sum Medium

377. Combination Sum IV Medium

935. Knight Dialer Medium

1223. Dice Roll Simulation Medium

416. Partition Equal Subset Sum Medium

808. Soup Servings Medium

790. Domino and Tromino Tiling Medium

801. Minimum Swaps To Make Sequences Increasing

673. Number of Longest Increasing Subsequence Medium

63. Unique Paths II Medium

576. Out of Boundary Paths Medium

1269. Number of Ways to Stay in the Same Place After Some Steps Hard

1220. Count Vowels Permutation Hard
### Merging Intervals

### DP on Strings

### Decision Making

