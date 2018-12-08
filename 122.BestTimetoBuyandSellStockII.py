class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        i = 0
        max_p = 0
        while i < n-1:

            while i < n - 1 and prices[i] >= prices[i+1]:
                i = i + 1
            valley = prices[i]
            while i < n - 1 and prices[i] <= prices[i+1]:
                i = i + 1
            peak = prices[i]                
            max_p = max_p + peak - valley

            
        return max_p
