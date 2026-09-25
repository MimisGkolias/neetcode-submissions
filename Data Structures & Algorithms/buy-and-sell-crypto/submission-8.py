class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, res = 0, 1, 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r += 1
            else:
                if profit > res:
                    res = profit
                r += 1
        return res