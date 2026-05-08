class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        openbrackets = "({["
        closedbrackets = ')}]'
        stack = []
        pairing = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for i in range(len(s)):
            if s[i] in openbrackets:
                stack.append(s[i])
            else:
                if not stack: return False
                if pairing[s[i]] != stack.pop():
                    return False
            
        if stack:
            return False
        else:
            return True
