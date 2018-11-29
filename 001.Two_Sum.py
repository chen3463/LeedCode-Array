class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = nums
        for i in range(0, len(nums)):
            L = L[1:]

            if target - nums[i] in L:           
                return [i, (L.index(target - nums[i])+i+1)]
                
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

          
        L = {}
        for i in range(len(nums)):
            if nums[i] in L: 
                return [L[nums[i]], i]
            comp = target - nums[i]
            L[comp] = i
