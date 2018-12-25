class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        s = len(nums)
        e = 0
        for i in range(len(nums)):
            if nums[i] != nums_sorted[i]:
                s = min(s, i)
                e = max(s, i)
        return e - s + 1 if e - s >=0 else 0
