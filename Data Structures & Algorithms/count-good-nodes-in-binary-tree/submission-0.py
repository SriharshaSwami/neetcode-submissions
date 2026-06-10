# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stk = [(root, -101)]
        count = 0
        while stk:
            node, largest = stk.pop()
            if node.val >= largest:
                count += 1
            largest = max(largest, node.val)
            if node.left: stk.append((node.left, largest))
            if node.right:stk.append((node.right, largest))

        return count


