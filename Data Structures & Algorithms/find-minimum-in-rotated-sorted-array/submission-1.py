class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] == nums[r]:
                return nums[m]
            else:
                if nums[m-1] > nums[m]:
                    return nums[m]
                r = m - 1
        
            
        
            