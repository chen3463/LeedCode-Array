class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = [[]]
        for num in nums:
            re = re + [[num]+i for i in re]
            
        return re
