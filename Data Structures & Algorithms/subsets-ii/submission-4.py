class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        def backtracking(i):
            if i >= len(nums):
                res.append(temp[:])
                return
            
            temp.append(nums[i])
            backtracking(i+1)

            temp.pop()
            # if nums[i] in temp:
            #     return 
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtracking(i+1)
        
        backtracking(0)
        return res
