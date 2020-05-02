'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = - sys.maxint - 1
        max_end = 0
        for i in range(len(nums)):
            max_end = max_end + nums[i]
            if max_sum < max_end:
                max_sum = max_end
                
            if max_end < 0:
                max_end = 0
            print max_sum, max_end
        return max_sum

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_history = -sys.maxsize
        max_end = 0
        max_i = 0
        for i in range(0, len(nums)):
            max_end += nums[i]
            # print(max_end, nums[i])
            max_i = max(max_end, nums[i])
            max_end = max_i
            if max_i > max_history:
                max_history = max_i

        return max_history
            max_end = max_i
            if max_i > max_history:
                max_history = max_i

        return max_history    
