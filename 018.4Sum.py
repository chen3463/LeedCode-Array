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
