'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.



'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        suffix = [nums[-1]]
        while (n - 2 - i) >= 0:

            if nums[n - 2 - i] >= nums[n - 1 - i]:
                suffix =  suffix + [nums[n - 2 - i]]
            else:
                break
            # print(n-i-1)
            i = i + 1
        # print(suffix)
            
        if n-i-2 >=0:
            for j in range(len(suffix)):
                if nums[n-i-2] < suffix[j]:
                    temp = nums[n-i-2]
                    nums[n-i-2] = nums[n-j-1]
                    # nums[n-j-1] = temp
                    suffix[j] =temp
                    break
        # print(suffix)
        nums[n-i-1:] = sorted(suffix)
