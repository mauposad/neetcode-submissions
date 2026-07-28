class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r  = 0, 1
        profit = 0
        while r < len(prices):
            trade_value = prices[r]-prices[l]
            if trade_value > 0:
                profit = max(profit, trade_value)
                r+=1
            elif trade_value < 0: 
                l=r
                r+=1
            else:
                r+=1
        return profit