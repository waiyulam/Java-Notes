from collections import defaultdict 

class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp_prep = [1 for i in range(10)]
        MOD = pow(10,9) + 7
        moves = defaultdict(int)
        moves[0] = [4,6]
        moves[1] = [6,8]
        moves[2] = [7,9]
        moves[3] = [4,8]
        moves[4] = [3,9,0]
        moves[5] = []
        moves[6] = [1,7,0]
        moves[7] = [6,2]
        moves[8] = [1,3]
        moves[9] = [2,4]
        
        for n in range(N-1):
            dp_cur = [0 for _ in range(10)]
            for i in range(10):
                for m in moves[i]:
                    dp_cur[i] += dp_prep[m]
            dp_prep = dp_cur[:]
        return sum(dp_prep) % MOD

                
if __name__ == "__main__":
    s = Solution()
    N = 3
    print("Output : {}".format(s.knightDialer(N)))