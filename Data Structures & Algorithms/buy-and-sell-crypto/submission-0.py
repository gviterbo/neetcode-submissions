class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        m = prices[0]
        for i in range(len(prices)):
            if prices[i] <= m:
                m = prices[i]
            else:
                ans = max(ans, prices[i]-m)
        return ans