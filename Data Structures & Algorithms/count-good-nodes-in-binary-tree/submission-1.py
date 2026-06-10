# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, largest):
            if not node:
                return 0
            
            res = 1 if node.val >= largest else 0
            largest = max(largest, node.val)
            res += dfs(node.left, largest)
            res += dfs(node.right, largest)
            return res
        return dfs(root, float("-inf"))