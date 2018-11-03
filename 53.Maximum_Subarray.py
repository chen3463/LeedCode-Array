class Solution(object):
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
