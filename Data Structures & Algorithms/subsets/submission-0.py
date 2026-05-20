class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtracking(i):
            if i == len(nums):
                res.append(sol[:]) #appending copy of sol
                return 
            
            #left side - not choosing the num first, i.e. only []
            backtracking(i+1)

            #right side - choosing the num, eg. [1]
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop() #this is the backtracking step, removing the num

        backtracking(0)
        return res