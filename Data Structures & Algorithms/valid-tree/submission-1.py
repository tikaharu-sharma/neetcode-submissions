class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False

        ## In this solution, I used the property that from one node
        ## in the tree, we can dfs into every other node as all nodes 
        ## should be connected in the tree
        
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
        #The visited set should contain all the nodes if it is a valid tree
        return len(visited) == n


        
        
        
        