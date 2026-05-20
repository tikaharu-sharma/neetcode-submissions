class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(i, current, total):
            if total == target:
                res.append(current[:])
                return
            if total > target or i >= len(nums):
                return 

            current.append(nums[i])
            backtracking(i, current, total + nums[i])
            current.pop()

            backtracking(i+1, current, total)
        
        backtracking(0, [], 0)
        return res