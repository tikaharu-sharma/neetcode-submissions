class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t)>len(s):
            return ""
        countS, countT = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        have, need = 0, len(countT)
        result = [-1, -1]
        reslen = 10000
        l = 0

        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)

            if s[r] in t and countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                length = r - l + 1
                if length < reslen:
                    result = [l, r]
                    reslen = length
                
                countS[s[l]] -= 1
                if s[l] in t and countS[s[l]]<countT[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        if reslen == 10000:
            return ""
        else:
            return s[l:r+1]

