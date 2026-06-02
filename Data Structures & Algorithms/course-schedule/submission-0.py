class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            hmap[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if hmap[course] == []:
                return True
            visited.add(course)
            for prereq in hmap[course]:
                if not dfs(prereq):
                    return False
                
            visited.remove(course)
            hmap[course] = []
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True