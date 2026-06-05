class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        
        hmap = {i:[] for i in range(n)}
        for a, b in edges:
            hmap[a].append(b)
            hmap[b].append(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for child in hmap[node]:
                dfs(child)
        
        dfs(0)
        return len(visited) == n


        
        
        
        