class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visit = set()

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(cur, prev):
            if cur in visit:
                return False
            visit.add(cur)
            for nei in graph[cur]:
                if nei == prev: continue
                if not dfs(nei, cur):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n