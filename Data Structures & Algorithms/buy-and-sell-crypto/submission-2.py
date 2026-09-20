class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        index = 0
        max_profit = 0
        min_number = 1000000
        while index < len(prices):
            
            min_number = min(min_number, prices[index])

            max_profit = max(max_profit, prices[index] - min_number)
            index += 1
        return max_profit



        