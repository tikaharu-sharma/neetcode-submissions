class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hmap = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in hmap:
                ans = max(ans, r-l)
                l = max(l,hmap[s[r]] + 1)
            hmap[s[r]] = r
        
        ans = max(ans, r-l+1)
        return ans

            