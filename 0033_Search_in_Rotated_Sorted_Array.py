'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1





C1. 1 2 3 4 5 6 7 8 9
C2. 3 4 5 6 7 8 0 1 2
C3. 7 8 9 1 2 3 4 5 6
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        if n == 0:
            return -1
        if target == nums[0]:
            return l
        if target == nums[r]:
            return r 
        mid = int((r + l) / 2)
        print(mid)
        if nums[mid] == target:
            return mid
        else:
            return self.binary(nums, target, l, r)
                      
                
    def binary(self, nums, target, l, r):
        if target == nums[l]:
            return l
        if target == nums[r]:
            return r 
            
        mid = int((r + l) / 2)
        print(mid)
        if nums[mid] == target:
            return mid
        else:
            if nums[mid] < nums[r] and nums[mid] > nums[l]:
                if nums[mid] > target and target > nums[l]:
                    return self.binary(nums, target, l, mid-1)
                else:
                    return self.binary(nums, target, mid+1, r)
                
            if nums[mid] > nums[r] and nums[mid] > nums[l]:
                if nums[mid] > target and target > nums[l]:
                    return self.binary(nums, target, l, mid-1)
                else:
                    return self.binary(nums, target, mid+1, r)
                
            
            if nums[mid] < nums[r] and nums[mid] < nums[l]:
                if target < nums[mid] or target > nums[l]:
                    return self.binary(nums, target, l, mid-1)
                else:
                    return self.binary(nums, target, mid+1, r)
                
        return -1


