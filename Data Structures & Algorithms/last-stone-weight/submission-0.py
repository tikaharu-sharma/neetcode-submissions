class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) != 1:
            a = stones.pop()
            b = stones.pop()
            stones.append(a-b)
            stones.sort()
        return stones.pop()