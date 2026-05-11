class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        maxVal = 0
        minPrice = prices[0]

        if len(prices) == 1: 
            return 0 

        for i in range(1,len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else: 
                maxVal = max(prices[i]-minPrice, maxVal)
        
        return maxVal

