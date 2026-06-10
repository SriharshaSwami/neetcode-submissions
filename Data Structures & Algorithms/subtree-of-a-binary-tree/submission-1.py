# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.valid = False
        def sameTree(p, q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p) or (p.val != q.val):
                return False
            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)
            return left and right

        def inorder(node):
            if not node or self.valid:
                return 
            inorder(node.left)
            if sameTree(node, subRoot):
                self.valid = True
                return 
            inorder(node.right)

        inorder(root)
        return self.valid
        

