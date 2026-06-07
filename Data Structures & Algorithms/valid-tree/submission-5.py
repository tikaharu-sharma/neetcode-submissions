class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ##check previous submission for better solution
        if len(edges) != n-1:
            return False

        hmap = {i:[] for i in range(n)}
        for a,b in edges:
            hmap[a].append(b)
            hmap[b].append(a)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for child in hmap[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

        
        