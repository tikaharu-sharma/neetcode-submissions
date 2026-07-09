class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(src, target, visited):
            if src in visited: #found the target
                return False
            if src == target:  #already explored the node
                return True
            visited.add(src)

            for neighbor in graph[src]:
                if dfs(neighbor, target, visited):
                    return True
            
            return False #target not recheable from source
        
        for a,b in edges:
            visited = set()

            if dfs(a, b, visited):
                return [a,b]
            
            graph[a].append(b)
            graph[b].append(a)

            