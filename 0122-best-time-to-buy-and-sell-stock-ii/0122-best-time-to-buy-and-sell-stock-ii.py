class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #no matter what you do if you just subtract the difference between the number of one less itll make sense
        
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit