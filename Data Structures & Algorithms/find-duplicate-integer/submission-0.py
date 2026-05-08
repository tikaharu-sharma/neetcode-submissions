class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k = 0
        while nums[k] != -1:
            temp = nums[k]
            nums[k] = -1
            k = temp
        return k 