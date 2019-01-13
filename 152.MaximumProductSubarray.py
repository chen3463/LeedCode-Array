class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        re = nums[0]
        imax = re
        imin = re
        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = imax
                imax = imin
                imin = temp
            
            imax = max(nums[i], imax*nums[i])
            imin = min(nums[i], imin*nums[i])
            
            re = max(re, imax)
        
        return re
