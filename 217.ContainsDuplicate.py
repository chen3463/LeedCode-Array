class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = collections.Counter(nums)
        if len(counts.keys()) == sum(counts.values()):
            return False
        else:
            return True
