# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root is None:
            return -1
        ldepth = 1 + self.helper(root.left)
        rdepth = 1 + self.helper(root.right)
        self.ans = self.ans and (abs(ldepth - rdepth) <= 1)
        return max(ldepth, rdepth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.helper(root)
        return self.ans