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

<details>
<summary><b>Practices</b></summary>

- [Min Cost Climbing Stairs](min_climbing_stairs)
- [Minimum Path Sum](mps)
- [**Coin Change**](coin_change)
- [Minimum Falling Path Sum](falling_path)
- [Minimum Cost For Tickets](cost_tickets)
- [2 Keys Keyboard](keyboard)
- [Perfect Squares](perfect_square)
- [**Last Stone Weight II**](stone2)
- [Triangle](triangle)
- [Ones and Zeroes](zerosones)
- [**Maximal Square**](maxsquare)
- [**Minimum Swaps To Make Sequences Increasing**](minSwap)
- [**Tiling a Rectangle with the Fewest Squares**](tilingrectangle)
- [**Dungeon Game**](Dungeon)
- [**Minimum Number of Refueling Stops**](refuelStop)

</details>

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
- [Climbing Stairs easy](climing_stairs)

- [Unique Paths Medium](uniquePaths)

- [Number of Dice Rolls With Target Sum Medium](rolldice)

<details>
<summary><b>Practices</b></summary>

Note : Some questions point out the number of repetitions, in that case, add one more loop to simulate every repetition.

- [Knight Probability in Chessboard Medium](knight_chessboard)

- [**Target Sum Medium**](targetSum)

- [**Combination Sum IV Medium**](combinationSumIV)

- [Knight Dialer Medium](knightDialer)

- [**Dice Roll Simulation Hard**](rollSimulation)

- [Partition Equal Subset Sum Medium](partitionSum)

- [**Soup Servings Medium**](soupserving)

- [**Domino and Tromino Tiling Medium**](dominoTiling)

- [**Number of Longest Increasing Subsequence Medium**](LIS)

- [Unique Paths II Medium](uniquePath2)

- [Out of Boundary Paths Medium](outBoundary)

- [Number of Ways to Stay in the Same Place After Some Steps Hard](staySame)

- [Count Vowels Permutation Hard](vowelsPermutation)

</details>

### Merging Intervals

### DP on Strings

### Decision Making

