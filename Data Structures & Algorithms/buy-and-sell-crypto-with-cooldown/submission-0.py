class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #State DP problem, three states each day
        hold = -prices[0]
        sell = 0
        cooldown = 0

        for i in range(len(prices)):
            new_hold = max(hold, cooldown-prices[i])
            new_sell = hold + prices[i]
            new_cooldown = max(cooldown, sell)

            hold = new_hold
            sell = new_sell
            cooldown = new_cooldown
        
        return max(sell, cooldown)