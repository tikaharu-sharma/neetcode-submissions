class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dups = []
        for char in s:
            dups.append(char)
        for char in t:
            if char not in dups:
                return False 
            dups.remove(char)
        return True
        