class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) -1:
                dp[i] = 1
                continue
            
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i] and dp[j] > dp[i]:
                    dp[i] = dp[j]
                if nums[j] == nums[i] + 1:
                    break
            dp[i] += 1
        
        return max(dp)
