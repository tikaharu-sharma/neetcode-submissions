class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for source, dest, cost in flights:
            adj[source].append([dest, cost])
        
        result = [float('inf') for i in range(n)]
        
        q = deque()
        q.append([src, 0])

        ##Using bfs for k+1 times
        for _ in range(k+1):
            for _ in range(len(q)):
                airport, price = q.popleft()
                for next_dest, next_price in adj[airport]:
                    new_cost = price+next_price
                    if new_cost < result[next_dest]:
                        q.append([next_dest, new_cost])
                        result[next_dest] = new_cost
        
        return -1 if result[dst] == float('inf') else result[dst]