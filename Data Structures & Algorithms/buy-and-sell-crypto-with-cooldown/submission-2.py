class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #State DP problem, three states each day
        hold = -prices[0] #if you are holding the stock that day
        sell = 0 #if you are selling the stock that day
        cooldown = 0 #if you are not doing anything that day

        for i in range(len(prices)):
            new_hold = max(hold, cooldown-prices[i])
            new_sell = hold + prices[i]
            new_cooldown = max(cooldown, sell)

            hold = new_hold
            sell = new_sell
            cooldown = new_cooldown
        
        return max(sell, cooldown)