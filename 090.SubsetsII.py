class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = [[]]
        for num in nums:
            re = re + [sorted([num]+i) for i in re]
        re1 = []
        for item in re:
            if item not in re1:
                re1.append(item)
        return re1
