class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    queue.append((r,c,0))
        
        while queue:
            r, c, dist = queue.popleft()
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dirn in directions:
                nr, nc = dirn
                r_new, c_new = r + nr, c + nc
                if 0 <= r_new < row and 0 <= c_new < col and grid[r_new][c_new] == 2147483647:
                    grid[r_new][c_new] = dist + 1
                    queue.append((r_new,c_new, dist+1))
        