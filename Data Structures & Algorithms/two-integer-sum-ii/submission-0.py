class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one = 0
        two = 1
        while one < len(numbers):
            if numbers[one] + numbers[two] == target:
                return [one+1,two+1]
            if numbers[one] + numbers[two] > target or two == len(numbers) - 1:
                one += 1
                two = one + 1
            else:
                two += 1
            