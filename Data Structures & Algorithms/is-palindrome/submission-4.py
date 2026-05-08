class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        lower = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        first = 0
        last = len(s) - 1
        while first < last:
            while first<last and s[first] not in lower:
                first += 1
            while last>first and s[last] not in lower:
                last -= 1
            if s[first].lower() != s[last].lower():
                return False
            first += 1
            last -= 1
        return True