class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        minute = 0
        fresh = 0
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dirn in directions:
                    rr, cc = dirn
                    nr, nc = r + rr, c + cc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            minute += 1
        
        if fresh == 0:
            return minute
        else:
            return -1