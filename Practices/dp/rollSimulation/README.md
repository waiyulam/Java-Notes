# 1223. Dice Roll Simulation ( HARD )

A die simulator generates a random number from 1 to 6 for each roll. You
introduced a constraint to the generator such that it cannot roll the number i
more than rollMax[i] (1-indexed) consecutive times. 

Given an array of integers rollMax and an integer n, return the number of
distinct sequences that can be obtained with exact n rolls.

Two sequences are considered different if at least one element differs from each
other. Since the answer may be too large, return it modulo 10^9 + 7.
![](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/rollSimulation/562837831.jpeg)
## Examples 

```
Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.
``` 

```
Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30
```

```
Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181
```

## Constraint 
- 1 <= n <= 5000
- rollMax.length == 6
- 1 <= rollMax[i] <= 15

![](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/rollSimulation/562837831.jpeg) 
![](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/rollSimulation/562837832.jpeg)
![](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/rollSimulation/562837833.jpeg)
![](https://github.com/waiyulam/Interview-Prep-Guide/tree/master/Practices/dp/rollSimulation/562837834.jpeg)


