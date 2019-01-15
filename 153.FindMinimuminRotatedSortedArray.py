class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = 0
        e = n
        if n == 1:
            return nums[s]
        if nums[n-1] > nums[s]:
            return nums[s]
        mid = (s+e)//2
        if nums[mid] < nums[mid-1]:
            return nums[mid]
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[mid] > nums[s]:
            return self.findMin(nums[mid+1:])
        else:
            return self.findMin(nums[:mid])  
