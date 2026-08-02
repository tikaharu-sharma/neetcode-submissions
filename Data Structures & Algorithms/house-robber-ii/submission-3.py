class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        prev1 = 0
        prev2 = 0

        for i in range(len(nums)-1):
            curr1 = max(prev1, prev2+nums[i])
            prev2 = prev1
            prev1 = curr1
        
        prev1 = 0
        prev2 = 0

        for i in range(1, len(nums)):
            curr2 = max(prev1, prev2+nums[i])
            prev2 = prev1
            prev1 = curr2
        
        return max(curr1, curr2)
