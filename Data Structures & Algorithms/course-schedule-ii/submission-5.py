class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hmap = {i:[] for i in range(numCourses)}

        for cor,pre in prerequisites:
            hmap[cor].append(pre)

        state = [0] * numCourses
         # 0 - not visited
         # 1 - visiting
         # 2 - complete and safe
        ans = []
        
        def dfs(i):
            if state[i] == 1:
                return False
            if state[i] == 2:
                return True
            state[i] = 1

            for neighbour in hmap[i]:
                if not dfs(neighbour):
                    return False
            
            ans.append(i)
            state[i] = 2
            return True
        
        for num in range(numCourses):
            if not dfs(num):
                return []
        return ans
        


