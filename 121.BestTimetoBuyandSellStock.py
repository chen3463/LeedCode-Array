class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        max_profit = 0
        maxP = prices[-1]
        for i in reversed(range(1, len(prices))):
            maxP = max(prices[i], maxP)
            if maxP - prices[i-1] > max_profit:
                max_profit = maxP - prices[i-1]

        return max_profit
