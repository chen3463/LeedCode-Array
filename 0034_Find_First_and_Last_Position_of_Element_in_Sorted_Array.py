'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        l = 0
        r = len(nums) - 1

        re = self.binary(nums, target, l, r)

        if len(re) > 0:
            return [re[0], re[-1]]
        else:
            return [-1, -1]
        
            
    def binary(self, nums, target, l, r):
        re = []
        if l >= r:
            if target == nums[l]:
                re = re + [l]
            return re
        elif r - l == 1:
            
            if target == nums[l]:
                re = re + [l]
            if target == nums[r]:
                re = re + [r]
            return re
        else:
            
            mid = int((l+r) / 2)
            if nums[mid] == target:
                return re + self.binary(nums, target, l, mid-1) + [mid] + self.binary(nums, target, mid+1, r) 
            elif nums[mid] > target:
                return re + self.binary(nums, target, l, mid-1) 
            else:
                return re + self.binary(nums, target, mid+1, r) 

class Solution2:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # print(len(nums))
        if len(nums) == 0:
            return [-1, -1]
        re1 = self.findindex(nums, target, True)
        if  len(nums)-1 < re1 or nums[re1] != target:
            return [-1, -1]
        re2 = self.findindex(nums, target, False)
        return [re1, re2-1]
    
    def findindex(self, nums, target, start):
        right = len(nums) 
        left = 0
        while left < right:
            mid = int((right + left) / 2)
            if nums[mid] > target or (start and nums[mid] == target):
                right = mid
            else:
                left = mid + 1
            
        return left

class Solution3:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        re = [self.binary_left(nums, target), self.binary_right(nums, target)]

        if len(re) > 0:
            return [re[0], re[-1]]
        else:
            return [-1, -1]
        
            
    def binary_left(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + int((r-l) / 2)
            print('left', nums[l], nums[r], nums[m])
            if target <= nums[m]:
                r = m - 1
            else: #target > nums[m]:
                l = m + 1
            
        if (l >= 0 and l < len(nums) ) and nums[l] == target:
            return l
        
        return -1
    
    
    def binary_right(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + int((r-l) / 2)
            print('right', nums[l], nums[r], nums[m])
            if target < nums[m]:
                r = m - 1
            elif target >= nums[m]:
                l = m + 1
            
        if (r >= 0 and r <= len(nums) - 1) and nums[r] == target:
            return r
        
        return -1
