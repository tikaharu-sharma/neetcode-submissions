class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)]
        heapq.heapify(minHeap)
        visit = set()
        row , col = len(grid), len(grid[0])
        dirn = [(1,0),(0,1),(-1,0),(0,-1)]

        while True:
            elevation, r, c = heapq.heappop(minHeap)

            if (r,c) in visit:
                continue
            visit.add((r,c))
            
            if r==row-1 and c==col-1:
                return elevation

            for nr, nc in dirn:
                r_new = r+nr
                c_new = c+nc
                if 0<=r_new<row and 0<=c_new<col and (r_new,c_new) not in visit:
                    new_elevation = max(elevation, grid[r_new][c_new])
                    heapq.heappush(minHeap, (new_elevation, r_new, c_new))