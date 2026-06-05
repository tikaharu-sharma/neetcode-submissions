class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = {i:[] for i in range(n)}
        
        for a, b in edges:
            hmap[a].append(b)
            hmap[b].append(a)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for child in hmap[node]:
                dfs(child)

        ans = 0
        for key in hmap:
            if key not in visit:
                dfs(key)
                ans += 1
        return ans

        


        