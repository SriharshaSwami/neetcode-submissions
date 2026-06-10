# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minVal, maxVal):
            if not node:
                return True
        
            if node.val <= minVal or node.val >= maxVal:
                return False
            lst = dfs(node.left, minVal, node.val)
            rst = dfs(node.right, node.val, maxVal)
            return lst and rst
        return dfs(root, float("-inf"), float("inf"))
        
        