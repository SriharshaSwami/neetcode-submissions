class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # write your code here

        par = [i for i in range(n)]
        rank = [1] * n
        
        def find(n1):
            res = n1
            while res != par[res]:
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            elif rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return 1
        res = n
        for i, j in edges:
            res -= union(i, j)
        return res