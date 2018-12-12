class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        n = len(nums)
        
        if n <=2:
            return max(nums)
        else:
            print nums
            return nums[n-3]
