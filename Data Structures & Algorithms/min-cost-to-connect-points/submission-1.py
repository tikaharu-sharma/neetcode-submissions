class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
            return dist

        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0,0))
        total_dist = 0
        visit = set()

        while len(visit) != len(points):
            dist, index = heapq.heappop(minHeap)
            if index in visit:
                continue
            visit.add(index)
            total_dist += dist

            for i in range(len(points)):
                if i in visit:
                    continue
                length = manhattan(points[index], points[i])
                heapq.heappush(minHeap, (length, i))
        
        return total_dist
                
                