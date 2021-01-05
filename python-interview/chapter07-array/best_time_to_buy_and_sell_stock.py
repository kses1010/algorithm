# 121. Best Time to Buy and Sell Stock

import sys

# 완전 탐색
from math import inf


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                profit = max(prices[j] - price, profit)
        return profit


# 저점 고점 문제 - 카데인 알고리즘 O(n)
class Solution2:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        min_price = inf

        for i in prices:
            min_price = min(min_price, i)
            profit = max(profit, i - min_price)

        return profit


sol = Solution()
sol2 = Solution2()
stock1 = [7, 1, 5, 3, 6, 4]
stock2 = [7, 6, 4, 3, 1]
stock3 = [2, 4, 1]
print(sol.maxProfit(stock1))
print(sol.maxProfit(stock2))
print(sol.maxProfit(stock3))
print('----------')
print(sol2.maxProfit(stock1))
print(sol2.maxProfit(stock2))
print(sol2.maxProfit(stock3))
