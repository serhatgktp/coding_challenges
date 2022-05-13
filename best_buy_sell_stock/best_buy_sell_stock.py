class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        
        left = 0
        right = 1
        
        if len(prices) < 2:
            return 0
        
        while right < len(prices):
            if prices[right] - prices[left] > max_profit:
                max_profit = prices[right] - prices[left]
            elif prices[right] < prices[left]:
                left = right
            right += 1
        
        return max_profit