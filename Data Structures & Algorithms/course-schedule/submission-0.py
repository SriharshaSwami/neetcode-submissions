class Solution:
    def canFinish(self, numCourses: int, edges: List[List[int]]) -> bool:
        req = {}

        for i in range(numCourses):
            req[i] = []

        for i, j in edges:
            req[i].append(j)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if req[course] == []:
                return True
            visited.add(course)
            for pre in req[course]:
                if not dfs(pre): return False
            visited.remove(course)

            return True
        for c in range(numCourses):
            if not dfs(c): return False
        return True
