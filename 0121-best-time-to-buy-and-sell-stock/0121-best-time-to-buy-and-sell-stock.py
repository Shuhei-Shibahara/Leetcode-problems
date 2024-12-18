class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in range(1,len(prices)):
            if buy_price > prices[p]:
                buy_price = prices[p]
            
            profit = max(profit, prices[p] - buy_price)
        
        return profit