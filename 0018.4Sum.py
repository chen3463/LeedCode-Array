class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        found = 0
        d = {}
        results = {}
        if len(nums) >= 4:
            for i in range(len(nums)-1):
                for j in range(i+1, len(nums)):
                    s = nums[i] + nums[j]
                    if not d.get(s):
                        d[s] = []
                    d[s].append([i,j])

        for i in d:
            if d.get(target-i):
                for m in d[i]:
                    for n in d[target - i]:
                        if m[0] != n[0] and m[1] != n[1] and m[0] != n[1] and m[1] != n[0]:
                            temp = m + n
                            temp = [nums[p] for p in temp]
                            temp.sort()
                            results[tuple(temp)] = 1

                found = 1

        if found == 0 or len(nums) < 4:
            return []

        return list(results.keys())
    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 1. sort the array
        nums.sort()
        
        # 2. Call kSum with start = 0, k = 4, and target
        return self.kSum(nums, target, 4)
    
    def kSum(self, nums, target, k):
        res = []
        if len(nums) == 0 or nums[0]*k > target or nums[-1]*k < target:
            return res
        if k == 2:
            return self.twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for _, re in enumerate(self.kSum(nums[i+1:], target-nums[i], k-1)):
                    res.append([nums[i]] + re)
                    # print(res)

        return res

    def twoSum(self, nums, target):
        res = []
        left = 0
        right = len(nums)-1
            
        while (left < right):
            twosum = nums[left] + nums[right]
            if target == twosum:
                res.append([nums[left], nums[right]])
                left = left + 1
                right = right - 1          
                    
            elif target > twosum or (left > 0 and nums[left] == nums[left-1]):
                left = left + 1

            elif target < twosum or (right < len(nums)-1 and nums[right] == nums[right+1]):
                right = right - 1
                                    
        return res
        

