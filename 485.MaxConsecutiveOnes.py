class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        max_n = 0
        temp = 0
        for i in range(len(nums)):
            
            if nums[i] == 1:
                temp = temp + 1
            else:
                max_n = max(temp, max_n)
                temp = 0
        max_n = max(temp, max_n)
        return max_n
