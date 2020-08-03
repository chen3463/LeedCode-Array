'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left, right = 0, len(numbers)-1
        
        while left < right:
            twosum = numbers[left] + numbers[right]
            if twosum == target:
                res = [left+1, right+1]
                left += 1
                right -= 1
            if target > twosum or (left > 0 and numbers[left] == numbers[left-1]):
                left += 1
            if target < twosum or (right < len(numbers)-1 and numbers[right] == numbers[right+1]):
                right -= 1
        
        return res
