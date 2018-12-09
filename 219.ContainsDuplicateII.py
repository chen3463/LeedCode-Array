class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        L = {}
        for i in range(len(nums)):
            if nums[i] in L.keys():
                if i - L[nums[i]] <= k:
                    return True
                else:
                    L[nums[i]] = i
            else:
                L[nums[i]] = i
                
        return False
            
