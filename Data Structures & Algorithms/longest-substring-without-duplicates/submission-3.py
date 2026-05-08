class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        left = 0
        right = 1
        res = 0
        length = 1
        dup = set()
        dup.add(s[left])
        while left < len(s)-1:
            if s[right] in dup:
                res = max(res, length)
                left += 1
                right = left + 1
                length = 1
                dup = set()
                dup.add(s[left])
            elif right == len(s) - 1:
                res = max(res, length+1)
                return res
            else:
                dup.add(s[right])
                right += 1
                length += 1
        return res

