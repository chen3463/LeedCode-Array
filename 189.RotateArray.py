class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        temp = nums[0:(n-k)]
        for i in range(k):
            nums[i] = nums[n-k+i]
        for j in range(len(temp)):
            nums[k+j] = temp[j]
