# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root is None:
            return int(1e9)
        if root.left is None and root.right is None:
            return 1
        return min(1 + self.helper(root.left), 1 + self.helper(root.right))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.helper(root)