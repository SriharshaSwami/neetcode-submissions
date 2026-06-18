# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                if node.val >= node.right.val:return False
                stack.append(node.right)
            if node.left:
                if node.val <= node.left.val:return False
                stack.append(node.left)
            
        return True

        


















