class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        p = prices[0]
        for i in range(1, n):
            if prices[i] < prices[i-1]:
                ans += prices[i-1]-p
                p = prices[i]
        return ans + prices[n-1] - p