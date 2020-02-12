'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            
            if len([i for i in str(num)]) % 2 == 0:
                res += 1
        return res
