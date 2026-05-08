class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_sequence = 0

        for num in nums:
            if num-1 not in num_set:
                sequence = 1
                while(num+1) in num_set:
                    sequence += 1
                    num += 1
                max_sequence = max(max_sequence, sequence)
        return max_sequence
