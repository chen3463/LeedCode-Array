'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''
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
        
  class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        for i in range(-1, -len(digits)-1, -1):
            print(i, digits[i])
            if i == -1 and digits[i] + 1 >= 10:
                digits[i] = digits[i] + 1 -10
                digits[i-1] = digits[i-1] + 1
            elif i == -1:
                digits[i] = digits[i] + 1
            elif digits[i] >= 10:
                digits[i] = digits[i] - 10
                digits[i-1] = digits[i-1] + 1
                
        if digits[0] == 0: 
            return digits[1:] 
        else: 
            return digits
                
                
                
            
        return str(sum_d)
