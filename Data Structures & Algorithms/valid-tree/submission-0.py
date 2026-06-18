class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) == n - 1:
            return True
            
        adj_list = defaultdict(list)
        for i, nei in edges:
            adj_list[i].append(nei)
            adj_list[nei].append(i)

        nodes = adj_list.keys()
        # Lets run DFS with visited
        visited = set()
        def dfs(u, par):
            if u in visited:
                return False
            
            visited.add(u)
            for nei in adj_list[u]:
                if nei == par:
                    #skip
                    continue
                if not dfs(nei, par):
                    return False
                 
        return dfs(0, -1) and len(visited) == n


