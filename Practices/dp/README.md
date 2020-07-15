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
- [Min Cost Climbing Stairs](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/climbing_stairs.py)
- [Minimum Path Sum](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/mps.py)
- [**Coin Change**](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/coin_change.py)
- [Minimum Falling Path Sum](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/falling_path.py)
- [Minimum Cost For Tickets](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/cost_tickets.py)
- [2 Keys Keyboard](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/keyboard.py)
- [Perfect Squares](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/perfect_square.py)
- [**Last Stone Weight II**](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/stone2.py)
- [Triangle](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/triangle.py)
- [Ones and Zeroes](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/zerosones.py)
- [**Maximal Square**](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/maxsquare.py)
- Coin Change
- Tiling a Rectangle with the Fewest Squares
- Dungeon Game
- Minimum Number of Refueling Stops

### Distinct Ways


### Merging Intervals

### DP on Strings

### Decision Making

