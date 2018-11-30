class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x == 10:
            return False
        L = []
        o = x
        while o >= 10:
            # print o % 10
            L = [o % 10] + L
            o = o / 10 
            
            
        L = [o] + L
        # return L
        n = len(L)
        i=0
        while i < n/2:
            if L[i] != L[n-i-1]:
                return False
            i = i + 1
        return True
