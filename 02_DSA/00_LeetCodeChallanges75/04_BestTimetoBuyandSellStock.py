'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

class Solution:
    def maxProfit(self, prices) -> int:
        # brute force
        '''
        currentMax = 0
        for idx, val in enumerate(prices):
            for j in range(idx +1, len(prices)):
                if prices[j] - val > currentMax:
                    currentMax = prices[j] - val

        return currentMax
        '''
        
        i, j = 0, 1 # buy and sell index.
        currentMax = 0
        while j < len(prices):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                currentMax = max(currentMax, profit)
            else:
                i = j
            j += 1
        return currentMax

print(Solution.maxProfit(None, [7,1,5,3,6,4]))