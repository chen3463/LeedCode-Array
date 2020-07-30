'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

'''
DP program, check the results of each index, which can be then ending index of array
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_hist = - sys.maxint
        max_end = 0
        for i in range(len(nums)):
            max_end = max_end + nums[i]
            max_end = max(max_end, nums[i])
            if max_hist < max_end:
                max_hist = max_end
                
        return max_hist


