# Solution : https://leetcode.com/problems/maximal-square/solution/
# Triangle solution to reduce space complexity

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        max_l = 0
        
        for i in range(m):
            if matrix[i][0] == '1':
                max_l = 1
                
        for i in range(n):
            if matrix[0][i]) == '1':
                max_l = 1
          
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i-1][j]),int(matrix[i-1][j-1]),int(matrix[i][j-1])) + 1
                    max_l = max(max_l,matrix[i][j])
        
        return max_l*max_l
                    
if __name__ == "__main__":
    s = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print("Output: {}".format(s.maximalSquare(matrix)))