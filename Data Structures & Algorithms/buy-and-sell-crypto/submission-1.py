class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            lowest_buy = min(lowest_buy, prices[i])
            max_profit = max(max_profit, prices[i] - lowest_buy)

        return max_profit