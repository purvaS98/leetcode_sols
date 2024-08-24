class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy_price = 10000
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]

            if prices[i] - buy_price > max_profit:
                max_profit = prices[i] - buy_price

        
        return max_profit