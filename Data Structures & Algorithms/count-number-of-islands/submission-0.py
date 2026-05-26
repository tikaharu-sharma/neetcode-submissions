class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        ans = 0

        def dfs(r, c):
            if r<0 or c<0 or r==row or c==col or (r,c) in visited or grid[r][c] == "0":
                return 
            
            visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    ans += 1
                    dfs(r,c)
        return ans