class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n > 1:
            mid = n // 2
            left = nums[0:mid]
            right = nums[mid:]
            self.sortColors(left)
            self.sortColors(right)
        
            i = 0
            j = 0
            k = 0
            l_n = len(left)
            r_n = len(right)
            while i < l_n and j < r_n:
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i = i + 1
                else:
                    nums[k] = right[j]
                    j = j + 1
                k = k + 1
        
            while i < l_n:
                nums[k] = left[i]
                i=i+1
                k=k+1
        
            while j < r_n:
                nums[k] = right[j]
                j=j+1
                k=k+1
        
        
            
