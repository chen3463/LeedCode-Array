class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        
        i = 0
        a = len(nums)
        for j in range(0, a):
            if nums[i] != nums[j]:
                i = i + 1 
                # print nums[j], nums[i]
                nums[i] = nums[j]

                     
        return i+1
