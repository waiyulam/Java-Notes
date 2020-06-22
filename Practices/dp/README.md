# Dynamic Programming Patterns

## Patterns
- [Minimum (Maximum) Path to Reach a Target](#Minimum(Maximum)_Path)
- [Distinct Ways](#Distinct_Ways)
- [Merging Intervals](#Merging_Intervals)
- [DP on Strings](#DP_on_Strings)
- [Decision Making](#Decision_Making)

### Minimum(Maximum) Path
Generate problem statement for this pattern    
**Statement** : Given a target find minimum (maximum) cost / path / sum to reach the target.
**Approach** : Choose minimum (maximum) path among all possible paths before the current state, then add value for the current state.
```python
routes[i] = min(routes[i-1], routes[i-2], ... , routes[i-k]) + cost[i]
```


### Distinct Ways


### Merging Intervals

### DP on Strings

### Decision Making

