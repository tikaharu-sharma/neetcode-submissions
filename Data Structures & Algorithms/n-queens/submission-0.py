class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        temp = [["."] * n for i in range(n)]
        col = set()
        positive_diagonal = set() #r+c
        negative_diagonal = set() #r-c

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in temp]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in col or (r+c) in positive_diagonal or (r-c) in negative_diagonal:
                    continue
                col.add(c)
                positive_diagonal.add(r+c)
                negative_diagonal.add(r-c)
                temp[r][c] = "Q"
                backtracking(r+1)
                temp[r][c] = "."
                col.remove(c)
                positive_diagonal.remove(r+c)
                negative_diagonal.remove(r-c)
            
        backtracking(0)
        return res
                


        