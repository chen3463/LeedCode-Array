class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        sum_d = 0
        for i in range(n):
            sum_d = sum_d + digits[i]*(10**(n-i-1))
        sum_d = sum_d + 1
        return [int(x) for x in str(sum_d)]
