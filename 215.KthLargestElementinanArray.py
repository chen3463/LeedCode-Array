class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        print sorted(nums)
        nums = sorted(nums) # sorted(list(set(nums)))
        print nums
        n = len(nums)
        if n < k:
            return max(nums)
        else:
            return nums[n-k]
