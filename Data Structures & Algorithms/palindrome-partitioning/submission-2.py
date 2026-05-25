class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def backtrack(i):
            if i >= len(s):
                res.append(temp[:])
                return 
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if self.isPali(substring):
                    temp.append(substring)
                    backtrack(j+1)
                    temp.pop()
        backtrack(0)
        return res

    def isPali(self, string):
        return string == string[::-1]