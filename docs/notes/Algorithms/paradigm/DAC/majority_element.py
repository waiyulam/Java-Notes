'''
 Given an array of size n, find the majority element. The majority element is
 the element that appears more than ⌊ n/2 ⌋ times. You may assume that the array
 is non-empty and the majority element always exist in the array. Example 1:

    Input: [3,2,3] Output: 3 Example 2:

    Input: [2,2,1,1,1,2,2] Output: 2

 DAC Intuition: 

 If we know the majority element in the left and right halves of an array, we
 can determine which is the global majority element in linear time.

 DAC algorithms: 

 Here, we apply a classical divide & conquer approach that recurses on the left
 and right halves of an array until an answer can be trivially achieved for a
 length-1 array. Note that because actually passing copies of subarrays costs
 time and space, we instead pass lo and hi indices that describe the relevant
 slice of the overall array. In this case, the majority element for a length-1
 slice is trivially its only element, so the recursion stops there. If the
 current slice is longer than length-1, we must combine the answers for the
 slice's left and right halves. If they agree on the majority element, then the
 majority element for the overall slice is obviously the same[1]. If they
 disagree, only one of them can be "right", so we need to count the occurrences
 of the left and right majority elements to determine which subslice's answer is
 globally correct. The overall answer for the array is thus the majority element
 between indices 0 and 

Time complexity : O(nlgn)

Space complexity : O(lgn)

 Although the divide & conquer does not explicitly allocate any additional
 memory, it uses a non-constant amount of additional memory in stack frames due
 to recursion. Because the algorithm "cuts" the array in half at each level of
 recursion, it follows that there can only be O(lgn) "cuts" before the
 base case of 1 is reached. It follows from this fact that the resulting
 recursion tree is balanced, and therefore all paths from the root to a leaf are
 of length O(lgn). Because the recursion tree is traversed in a
 depth-first manner, the space complexity is therefore equivalent to the length
 of the longest path, which is, of course, O(lgn).
'''
class Solution(object):
    def majorityElement(self, nums):
        def majority_element_rec(l,h):
            # base case when l == h 
            if (l == h):
                return nums[l]
            else:
                mid = (l+h)//2
                m1 = majority_element_rec(l,mid)
                m2 = majority_element_rec(mid+1,h)
                if (m1==m2):
                    return m2
                count1 = sum(1 for i in range(l,h+1) if m1 == nums[i] )
                count2 = sum(1 for i in range(l,h+1) if m2 == nums[i])
                return m1 if count1 > count2 else m2
        return majority_element_rec(0,len(nums)-1)


if __name__ == "__main__":
    arr = [2,3,4,5,5,5]
    s = Solution()
    print(s.majorityElement(arr))