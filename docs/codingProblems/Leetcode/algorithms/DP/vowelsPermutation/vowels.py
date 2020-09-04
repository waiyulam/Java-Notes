class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 5
        kmod= int(1e9 + 7)
        # 'a''e''i''o''u' characters are represented by index 0

        # 用hashtable来存valid moves : 'e'->'a', 'i'->'e','a,e,o,u' -> 'i', 'i,u' -> 'o', 'a'->'u'
        validMoves = dict()
        validMoves[0] = [1]
        validMoves[1] = [0,2]
        validMoves[2] = [0,1,3,4]
        validMoves[3] = [2,4]
        validMoves[4] = [0]

        # 创建背包
        dp = [[0 for j in range (5)] for i in range(n)] 
        # 初始化值： 长度为1的array没有限制
        for i in range(5):
            dp[0][i] = 1
        
        for i in range(1,n):
            for j in range(5):
                for m in validMoves[j]:
                    dp[i][j] += dp[i-1][m]
                dp[i][j] %= kmod
        return sum(dp[n-1][:]) % kmod

    def countVowelPermutation_reduced(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 5
        kmod= int(1e9 + 7)
        # 'a''e''i''o''u' characters are represented by index 0

        # 用hashtable来存valid moves : 'e'->'a', 'i'->'e','a,e,o,u' -> 'i', 'i,u' -> 'o', 'a'->'u'
        validMoves = dict()
        validMoves[0] = [1]
        validMoves[1] = [0,2]
        validMoves[2] = [0,1,3,4]
        validMoves[3] = [2,4]
        validMoves[4] = [0]

        # 创建背包
        dp_prep = [0 for i in range (5)] 
        # 初始化值： 长度为1的array没有限制
        for i in range(5):
            dp_prep[i] = 1
        
        for i in range(1,n):
            dp_cur = [0 for i in range (5)] 
            for j in range(5):
                for m in validMoves[j]:
                    dp_cur[j] += dp_prep[m]
                dp_cur[j] %= kmod
            dp_prep = [dp_cur[i] for i in range (5)] 
            
        return sum(dp_prep[:]) % kmod


    def countVowelPermutation_pro(self,n):
        a, e, i, o, u = 1, 1, 1, 1, 1
        mod = 10**9+7
        for _ in range(1, n):
            a, e, i, o, u = (e+i+u)%mod, (a+i)%mod, (e+o)%mod, i%mod, (i+o)%mod
        return (a+e+i+o+u)%mod

if __name__ == "__main__":
    s = Solution()
    n = 144
    print("output: {}".format(s.countVowelPermutation(n)))

        

