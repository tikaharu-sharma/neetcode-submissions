class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()

            for s, d, cost in flights:
                if prices[s] != float('inf'):
                    temp[d] = min(temp[d], prices[s]+cost)
            
            prices = temp
        
        return -1 if prices[dst] == float('inf') else prices[dst]