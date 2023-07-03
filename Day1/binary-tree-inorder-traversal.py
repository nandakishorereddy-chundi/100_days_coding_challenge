# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.vals = []

    def helper(self, root):
        if root is None:
            return self.vals
        self.helper(root.left)
        self.vals.append(root.val)
        self.helper(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.helper(root)
        return self.vals