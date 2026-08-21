class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        result = max(nums)

        for num in nums:
            if num == 0:
                curMax, curMin = 1, 1
                continue
            
            temp = curMax * num
            curMax = max(temp, curMin * num, num)
            curMin = min(temp, curMin * num, num)
            result = max(result, curMax)
        
        return result