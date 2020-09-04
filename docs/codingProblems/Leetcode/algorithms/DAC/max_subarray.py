# small problem : l==h , element itself 
# crossing : max(sub1,sub2,cross)
import sys 

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxSubArray_rec(l,h):
            if (l==h):
                return nums[l]
            else:
                mid = (l+h)//2 
                sub1 = maxSubArray_rec(l,mid)
                sub2 = maxSubArray_rec(mid+1,h)
                # crossing problem 
                lmax = float('-inf')
                rmax = float('-inf')
                temp = 0
                for i in range(mid,l-1,-1):
                    temp += nums[i]
                    if temp > lmax:
                        lmax = temp 
                temp = 0
                for i in range(mid+1,h+1):
                    temp += nums[i]
                    if temp > rmax:
                        rmax = temp 
                return max(sub1,sub2,rmax+lmax)
        return maxSubArray_rec(0,len(nums)-1)


if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution()
    print(s.maxSubArray(arr))
        