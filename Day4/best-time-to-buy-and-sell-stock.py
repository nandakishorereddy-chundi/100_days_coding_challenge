class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        curr_min = int(1e5)
        mins = []
        for i in range(n):
            if prices[i] < curr_min:
                curr_min = prices[i]
            mins.append(curr_min)
        ans = 0
        for i in range(1, n):
            ans = max(ans, prices[i]-mins[i])
        return ans