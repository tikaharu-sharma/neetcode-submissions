class Solution:
    def numDecodings(self, s: str) -> int:
        prev1 = 1 
        prev2 = 0

        for i in range(len(s)-1,-1,-1):
            curr = 0

            #single digit
            if s[i] != '0':
                curr += prev1

            #double digit
            if i+1 < len(s) and 10<=int(s[i:i+2])<=26:
                curr += prev2
            
            prev2 = prev1
            prev1 = curr
        
        return prev1
