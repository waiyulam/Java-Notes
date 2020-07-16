class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        N = len(stations)
        # dp[i]: the farthest location we can get to using i refueling stops.
        dp = [-sys.maxsize for i in range(N+1)]
        dp[0] = startFuel
        for i in range(N):
            for t in reversed(range(i+1)):
                if (dp[t] >= stations[i][0]):
                    dp[t+1] = max(dp[t+1],dp[t]+stations[i][1])
        
        for i in range(N+1):
            if (dp[i] >= target):
                return i 
        return -1
        