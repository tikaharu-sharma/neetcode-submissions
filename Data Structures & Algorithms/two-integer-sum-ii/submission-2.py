class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        l = len(numbers) - 1
        while f < l:
            total = numbers[f] + numbers[l]
            if total == target:
                return [f+1,l+1]
            elif total < target:
                f += 1
            else:
                l -= 1
         
             