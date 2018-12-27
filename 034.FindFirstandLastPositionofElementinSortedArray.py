class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # print(len(nums))
        if len(nums) == 0:
            return [-1, -1]
        re1 = self.findindex(nums, target, True)
        if  len(nums)-1 < re1 or nums[re1] != target:
            return [-1, -1]
        re2 = self.findindex(nums, target, False)
        return [re1, re2-1]
    
    def findindex(self, nums, target, start):
        right = len(nums)
        left = 0
        while left < right:
            mid = int((right + left) / 2)
            if nums[mid] > target or (start and nums[mid] == target):
                right = mid
            else:
                left = mid + 1
            
        return left
