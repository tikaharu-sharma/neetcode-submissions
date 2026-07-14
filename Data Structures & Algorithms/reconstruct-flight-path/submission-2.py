class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        output = []
        flightList = defaultdict(list)
        for src, dest in tickets:
            flightList[src].append(dest)
        
        for src in flightList:
            flightList[src].sort(reverse=True)
        
        def dfs(city):
            while flightList[city]:
                new_city = flightList[city].pop()
                dfs(new_city)
            output.append(city)

        dfs("JFK")
        return output[::-1]
            
