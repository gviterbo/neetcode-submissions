class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for x in prices:
            maxP = max(maxP, x - minBuy)
            minBuy = min(x, minBuy)

        return maxP