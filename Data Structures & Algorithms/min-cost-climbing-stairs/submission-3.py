class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        var1 = 0
        var2 = cost[-1]

        for i in range(len(cost)-2, -1, -1):
            temp = cost[i] + min(var1, var2)
            var1 = var2
            var2 = temp
        
        return min(var1, var2)