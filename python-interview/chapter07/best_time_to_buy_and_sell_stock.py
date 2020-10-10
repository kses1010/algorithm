import sys


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                profit = max(prices[j] - price, profit)
        return profit


class Solution2:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        min_price = sys.maxsize

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
