#task: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)):
            if max(prices[i + 1:]) - prices[i] > profit:
                profit = max(prices[i + 1:] - prices[i])
        return profit