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
#### Practices 
- [Min Cost Climbing Stairs](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/min_climbing_stairs)
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
#### Examples 
- [Climbing Stairs easy](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/climing_stairs)

- [Unique Paths Medium](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/uniquePaths)

- [Number of Dice Rolls With Target Sum Medium](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/rolldice)


#### Practices 
Note : Some questions point out the number of repetitions, in that case, add one more loop to simulate every repetition.

- [Knight Probability in Chessboard Medium](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/knight_chessboard)

- [**Target Sum Medium**](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/targetSum)

- [**Combination Sum IV Medium**](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/combinationSumIV)

- [Knight Dialer Medium](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/knightDialer)

- [**Dice Roll Simulation Hard**](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/rollSimulation)

- [Partition Equal Subset Sum Medium](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/partitionSum)

- [**Soup Servings Medium**](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/soupserving)

- Domino and Tromino Tiling Medium

- Minimum Swaps To Make Sequences Increasing

- Number of Longest Increasing Subsequence Medium

- Unique Paths II Medium

- Out of Boundary Paths Medium

- Number of Ways to Stay in the Same Place After Some Steps Hard

- Count Vowels Permutation Hard
### Merging Intervals

### DP on Strings

### Decision Making

