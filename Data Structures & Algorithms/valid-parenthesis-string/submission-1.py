class Solution:
    def checkValidString(self, s: str) -> bool:
        ##tracking high and low open bracket

        low = 0
        high = 0

        for i, c in enumerate(s):
            if c == "(":
                low += 1
                high += 1
            elif c == ")":
                low -= 1
                high -= 1
            else:
                low -= 1 #treat as closed bracket
                high += 1 #treat as open bracket
            
            if high < 0:
                return False
            
            low = max(low, 0)
        
        return low == 0
        


