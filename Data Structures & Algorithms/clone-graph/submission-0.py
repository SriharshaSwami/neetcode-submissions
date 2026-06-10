"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        o_to_n = {}
        start = node
        stack = [start]

        while stack:
            node = stack.pop()
            o_to_n[node] = Node(node.val)
            for nei in node.neighbors:
                if nei not in o_to_n:
                    stack.append(nei)
            
        for old, new in o_to_n.items():
            for nei in old.neighbors:
                new.neighbors.append(o_to_n[nei])

        return o_to_n[start]


