class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        L = []
        p = len(nums)
        for row in nums:
            L = L + row
            q = len(row)
        if r * c != p * q:
            return nums
        print L
        out = []
        for i in range(r):
            temp = L[0:c]
            out = out + [temp]
            L = L[c:]
        
        return out
