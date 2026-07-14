class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price = prices[0]
        best_profit = 0

        for i in range(len(prices)):

            if prices[i] < lowest_price:
                lowest_price = prices[i]

            else:
                current = prices[i] - lowest_price
                best_profit = max(best_profit, current)

        return best_profit
        