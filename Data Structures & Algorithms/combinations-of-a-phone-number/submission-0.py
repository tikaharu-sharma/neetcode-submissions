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
        temp = []

        def backtrack(i):
            if i >= len(digits):
                res.append("".join(temp))
                return 
            
            num = int(digits[i])
            word = hmap[num]

            for j in range(len(word)):
                temp.append(word[j])
                backtrack(i+1)
                temp.pop()
            
        backtrack(0)
        return res
