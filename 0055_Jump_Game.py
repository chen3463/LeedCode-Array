'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
'''


# python 2
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        n = len(nums)
        if n <= 1:
            return True
        else:
            i = n - 1
            j = n - 2
            while i > 1 and j >= 0:
                print(i, j)
                target = nums[i]
                temp = nums[j]
                if temp >= (i-j):
                    i = i - (i-j)
                    j = i -1
                else:
                    j = j - 1
        # print(i, j)
        if j >= 0:
            if i >= 1 and nums[j] < (i-j):
                return False
            else:
                return True
        else:
            if i >= 1 and nums[0] < (i-j):
                return False
            else:
                return True
 
 # Python3
 class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        j = len(nums) - 1
        
        while i >= 0:
            # print(i, i+nums[i], j) 
            if nums[i] + i >= j: # at least i steps to nums[i] 
                j = i
            i = i - 1
                
        return j == 0
