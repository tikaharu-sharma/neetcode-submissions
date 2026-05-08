class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        res = []
        for i in range(0, len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res