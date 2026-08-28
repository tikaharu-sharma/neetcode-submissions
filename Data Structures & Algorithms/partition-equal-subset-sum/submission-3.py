class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total/2
        dp = set()
        dp.add(0)

        for num in nums:
            temp_dp = set()
            for n in dp:
                temp_dp.add(n+num) #add new sum
                temp_dp.add(n)     #add old sum
            dp = temp_dp
            if target in dp:
                return True
        return False


