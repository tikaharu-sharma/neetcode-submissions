import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r

        while l <= r:
            mid = (l+r)//2
            hour = 0

            for num in piles:
                hour += math.ceil(num/mid)
            if hour > h:
                l = mid + 1
            else:
                r = mid - 1
                best = min(best, mid)
        
        return best

