class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        pairing = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for i in range(len(s)):
            if s[i] in "{[(":
                stack.append(s[i])
            else:
                if not stack or pairing[s[i]] != stack.pop():
                    return False
            
        return not stack
