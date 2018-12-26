class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)
        tmp = sys.maxint
        sign = 0
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                diff = total - target 
                if diff == 0:
                    return total
                elif abs(diff) < tmp:
                    tmp = abs(diff)
                    ans = total
                if diff < 0:
                    j = j + 1
                else:
                    k = k - 1
            # print i, diff, tmp, ans
        return ans
