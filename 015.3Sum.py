class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        nums = sorted(nums)
        results = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums)-1
            target = 0 - nums[i]
            while j < k:
                if target == nums[j] + nums[k]:
                    results = results + [[nums[i], nums[j], nums[k]]]
                    j = j + 1
                    k = k - 1
                    while j<k and nums[j] == nums[j-1]:
                           j = j + 1
                    while j<k and nums[k] == nums[k+1]:
                           k = k - 1
                elif target > nums[j] + nums[k]:
                    j = j+1
                else:
                    k = k-1
                # print i, j, k
        return results
