class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        profit = 0
        pos = -prices[0]
        for i in range(1, len(prices)):
            pos = max(pos, profit-prices[i])
            profit = max(profit, pos+prices[i]-fee)
        return profit