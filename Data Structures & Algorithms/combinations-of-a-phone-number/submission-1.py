class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        hmap = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }

        res = []

        def backtrack(i, curStr):
            if i >= len(digits):
                res.append(curStr)
                return 
            
            num = int(digits[i])
            word = hmap[num]

            for char in word:
                backtrack(i+1, curStr+char)
            
        backtrack(0, "")
        return res
