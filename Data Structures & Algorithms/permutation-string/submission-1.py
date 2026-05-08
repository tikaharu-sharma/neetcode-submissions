class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count1 = {}
        count2 = {}
        l = len(s1)
        for char in s1:
            count1[char] = 1 + count1.get(char, 0)
        for i in range(l):
            count2[s2[i]] = 1 + count2.get(s2[i], 0)
        if count1 == count2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                del count2[s2[l]]
            l += 1
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            if count1 == count2:
                return True
        return False
        
