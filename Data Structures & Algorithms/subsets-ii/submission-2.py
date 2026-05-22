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
            if nums[i] in temp:
                return 
            backtracking(i+1)
        
        backtracking(0)
        return res
