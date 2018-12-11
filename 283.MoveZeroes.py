class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        n = len(nums)
        L = []
        for i in range(n):
            if nums[i] == 0:
                j = j + 1
            else:
                L = L + [nums[i]]

        for k in range(len(L)):
            nums[k] = L[k]
        print nums
        for m in range(j):
            nums[len(L)+m] = 0
            
