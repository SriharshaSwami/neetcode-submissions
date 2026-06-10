class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        adj_list = defaultdict(list)
        for i, nei in edges:
            adj_list[i].append(nei)
            adj_list[nei].append(i)

        # Lets run DFS with visited
        visited = set()
        def dfs(u, prev):
            if u in visited:
                return False
            
            visited.add(u)
            for nei in adj_list[u]:
                if nei == prev:
                    #skip the one nei i.e visited befotr this
                    continue
                if not dfs(nei, u):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n


