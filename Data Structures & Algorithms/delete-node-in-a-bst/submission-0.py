# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left and root.right:
                return root.right
            elif not root.right and root.left:
                return root.left
            else:
                safe = root.right
                root.right = None
                cur = root.left
                while cur.right:
                    cur = cur.right
                cur.right = safe
                return root.left
        return root
        