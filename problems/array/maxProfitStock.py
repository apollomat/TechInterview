class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = 200000
        for value in prices:
            if value - min_price > max_profit:
                max_profit = value - min_price
            if min_price > value:
                min_price = value

        return max_profit
