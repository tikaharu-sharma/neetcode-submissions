class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max1 = max2 = max3 = 0

        for num1, num2, num3 in triplets:
            if num1 <= target[0] and num2 <= target[1] and num3 <= target[2]:
                max1 = max(max1, num1)
                max2 = max(max2, num2)
                max3 = max(max3, num3)
        
        if max1==target[0] and max2==target[1] and max3==target[2]:
            return True
        return False