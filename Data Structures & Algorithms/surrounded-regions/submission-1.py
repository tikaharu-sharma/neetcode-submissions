class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])

        def dfs(r, c):
            if r<0 or c<0 or r == row or c == col:
                return
            if board[r][c] == "X" or board[r][c] == "S":
                return 
            board[r][c] = "S"
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for c in range(col):
            if board[0][c] == "O":
                dfs(0, c)
            if board[row-1][c] == "O":
                dfs(row-1, c)
            
        for r in range(1, row-1):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][col-1] == "O":
                dfs(r, col-1)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
        
        



        