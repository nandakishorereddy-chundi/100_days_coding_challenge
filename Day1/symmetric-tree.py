# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, lchild, rchild):
        if lchild is None and rchild is None:
            return True
        if (lchild is not None and rchild is None) or (lchild is None and rchild is not None):
            return False
        return lchild.val == rchild.val and self.helper(lchild.left, rchild.right) and self.helper(lchild.right, rchild.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)