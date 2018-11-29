class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 0:
            L = [i for i in str(x)]
            s = 1
        else:
            L = [i for i in str(-x)]
            s = -1
        n = len(L)
        new = 0
        while n:
            new = new + int(L[n-1]) * (10 ** (n-1))
            n = n - 1
        results = new * s
        if results > 2**31 - 1 or results < -2** 31:
            return 0 
        return results
         
