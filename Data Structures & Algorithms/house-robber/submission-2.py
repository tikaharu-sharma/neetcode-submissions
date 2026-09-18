class Solution:
    def rob(self, nums: List[int]) -> int:
        v1, v2 = 0, 0

        for i in range(len(nums)-1, -1, -1):
            temp = v1
            v1 = max(v1, nums[i]+v2)
            v2 = temp
        
        return v1