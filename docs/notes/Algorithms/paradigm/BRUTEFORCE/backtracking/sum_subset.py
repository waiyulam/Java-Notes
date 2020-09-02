#!/bin/python
'''
Subset sum problem is to find subset of elements that are selected from a given
set whose sum adds up to a given number K. We are considering the set contains
non-negative values. It is assumed that the input set is unique (no duplicates
are presented).

Output : fixed size solution (0,1,0,1,0)
'''

class Solution():
    def __init__(self,n):
        self.w = [0]*n 
        self.n = n


    def isValid(self,selections,v,m):
        # sum of weights along path 
        left = sum([w for i,w in enumerate(self.w) if (selections[i] == 1)])
        # remaining sum 
        right = sum([self.w[i] for i in range(v+1,self.n)])
        if left > m:
            return False
        elif left+right < m:
            return False 
        return True

    def sumofsubsetUtil(self,m,v,selections):
        # Base case 
        if v == self.n:
            if (sum(w for i,w in enumerate(self.w) if (selections[i] == 1)) == m):
                return True 
            return False 
        # Recursive 
        for i in range(1,-1,-1):
            selections[v] = i
            if self.isValid(selections,v,m):
                if self.sumofsubsetUtil(m,v+1,selections):
                    return True 
            selections[v] = -1
        return False
        

    def sumofsubset(self,m):
        selections = [-1] * self.n
        if self.sumofsubsetUtil(m,0,selections):
            print(selections)
            return True
        print("Fail")
        return False


if __name__ == "__main__":
    s = Solution(6)
    s.w = [5,10,12,13,15,18]
    m = 23
    s.sumofsubset(m)

    