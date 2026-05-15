class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ## Implementation using min_heap
        ## See other submission for the implementation using the max_heap
        min_heap = []
        for point in points:
            dist = (point[0]**2 + point[1]**2) **(1/2)
            min_heap.append((dist, point[0], point[1]))
        
        heapq.heapify(min_heap)
        ans = []
        while k != 0:
            dist, x, y = heapq.heappop(min_heap)
            ans.append([x,y])
            k-=1
        return ans


        

