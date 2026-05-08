class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        prefix = 1
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            output.append(prefix)
        
        postfix = 1
        for i in range(len(nums)-2,-1,-1):
            postfix *= nums[i+1]
            output[i] *= postfix
        
        return output
        