class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-inf")
        min_price = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(prices[i] - min_price, max_profit)
            min_price = min(min_price, prices[i])

        if max_profit <= 0:
            return 0
        return max_profit
