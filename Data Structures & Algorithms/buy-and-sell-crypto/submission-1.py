class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        left, right = 0, 1
        res = 0
        while left < len(prices) - 1:
            if right == len(prices) or prices[right] <= prices[left]:
                left += 1
                right = left + 1
                continue
            price = prices[right] - prices[left]
            res = max(res, price)
            right += 1
        return res
            