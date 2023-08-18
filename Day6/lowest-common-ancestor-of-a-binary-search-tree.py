# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def LCA(self, root, p, q):
        if root is None:
            return
        #print(f'root: {root.val}, p: {p.val}, q: {q.val}')
        if root.val == p.val or root.val == q.val:
            return root
        elif root.val > p.val and root.val < q.val:
            return root
        elif root.val > p.val:
            return self.LCA(root.left, p, q)
        else:
            return self.LCA(root.right, p, q)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        return self.LCA(root, p, q)