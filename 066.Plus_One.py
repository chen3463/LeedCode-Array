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

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        L = []
        n = len(digits)
        for i in range(0, n):
            if i == 0:
                a = (digits[n-i-1] + 1) % 10
                b = (digits[n-i-1] + 1)/10
            else:
                a = digits[n-i-1] % 10
                b = digits[n-i-1]/10
            
            print a, b
            L = [a] + L 
            digits[n-i-2] += b
        if b == 1 > 0:
            L = [b] + L
        return L   
