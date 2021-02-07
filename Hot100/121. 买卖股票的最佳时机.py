class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        minBuy = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            minBuy = min(minBuy, prices[i])
            maxProfit = max(maxProfit, prices[i] - minBuy)
        return maxProfit

        