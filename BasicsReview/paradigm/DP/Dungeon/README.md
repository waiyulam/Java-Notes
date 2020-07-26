174. Dungeon Game 

The demons had captured the princess (P) and imprisoned her in the bottom-right
corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid.
Our valiant knight (K) was initially positioned in the top-left room and must
fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at
any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative
integers) upon entering these rooms; other rooms are either empty (0's) or
contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to
move only rightward or downward in each step.

**Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.**


**Example** : 
Input : [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output : 7 For example,
given the dungeon below, the initial health of the knight must be at least 7 if
he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

![](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/Dungeon/4CDAD80C1.jpeg)
![](https://github.com/waiyulam/Interview-Prep-Guide/blob/master/Practices/dp/Dungeon/4CDAD80C2.jpeg)