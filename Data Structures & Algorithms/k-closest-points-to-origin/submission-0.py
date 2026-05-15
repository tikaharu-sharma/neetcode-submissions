class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ##Implementation using max_heap
        max_heap = []
        for point in points:
            dist = (point[0]**2+point[1]**2)**(1/2)
            max_heap.append((dist,point[0],point[1]))

        heapq.heapify_max(max_heap)
        ans = []
        while len(max_heap) != 0:
            dist, x, y = heapq.heappop_max(max_heap)
            if len(max_heap) < k:
                ans.append([x,y])
        return ans

