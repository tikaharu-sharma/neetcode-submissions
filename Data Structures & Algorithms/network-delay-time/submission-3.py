class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = defaultdict(list)
        for u,v,t in times:
            adjList[u].append([v,t])

        edges = []
        heapq.heapify(edges)
        visited = set()

        heapq.heappush(edges, (0, k))

        while edges:
            dist, node = heapq.heappop(edges)
            if node in visited:
                continue
            visited.add(node)

            if len(visited) == n:
                return dist
            
            for v,t in adjList[node]:
                if v not in visited:
                    heapq.heappush(edges, (dist+t, v))
        
        return -1
