class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        n = len(nums)
        if n > max_num:
            return n
        
        return list(set(range(max_num+1)).difference(set(nums)))[0]
