class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        res = []

        def backtrack(o, c):
            if o == c and o == n:
                res.append("".join(temp))
                return 
            
            if o < n:
                temp.append("(")
                backtrack(o+1, c)
                temp.pop()
            
            if c < o:
                temp.append(")")
                backtrack(o, c+1)
                temp.pop()
            
        backtrack(0, 0)
        return res

            

