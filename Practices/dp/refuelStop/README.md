871. Minimum Number of Refueling Stops

A car travels from a starting position to a destination which is target miles
east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station
that is station[i][0] miles east of the starting position, and has station[i][1]
liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel
liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the
gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach
its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still
refuel there.  If the car reaches the destination with 0 fuel left, it is still
considered to have arrived.

**Note**:

1 <= target, startFuel, stations[i][1] <= 10^9 
0 <= stations.length <= 500 
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target

**Approach 1: Dynamic Programming Intuition**

Let's determine dp[i], the farthest location we can get to using i refueling
stops. This is motivated by the fact that we want the smallest i for which dp[i]
>= target.

**Algorithm**

Let's update dp as we consider each station in order. With no stations, clearly
we can get a maximum distance of startFuel with 0 refueling stops.

Now let's look at the update step. When adding a station station[i] = (location,
capacity), any time we could reach this station with t refueling stops, we can
now reach capacity further with t+1 refueling stops.

For example, if we could reach a distance of 15 with 1 refueling stop, and now
we added a station at location 10 with 30 liters of fuel, then we could
potentially reach a distance of 45 with 2 refueling stops.

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in xrange(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1

**Complexity Analysis**

Time Complexity: O(N^2) where NN is the length of stations.

Space Complexity: O(N)O(N), the space used by dp.

