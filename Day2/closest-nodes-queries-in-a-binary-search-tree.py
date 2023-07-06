# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''

TLE because the tree may not be balanced. So, we need to balance the tree first.

class Solution:
    def traverse(self, root, to_find):
        if root is None:
            return
        if root.val > to_find:
            self.big = root.val
            self.traverse(root.left, to_find)
        if root.val == to_find:
            self.low = self.big = root.val
            return
        if root.val < to_find:
            self.low = root.val
            self.traverse(root.right, to_find)

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        output = []
        for query in queries:
            self.low = self.big = -1
            self.traverse(root, query)
            output.append([self.low, self.big])
        return output
'''

class Solution:
    def traverse(self, root, to_find):
            if root is None:
                return
            if root.val > to_find:
                self.big = root.val
                self.traverse(root.left, to_find)
            if root.val == to_find:
                self.low = self.big = root.val
                return
            if root.val < to_find:
                self.low = root.val
                self.traverse(root.right, to_find)

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # Balance the BST
        def balanceBST(root):
            arr = []
            def inorder(root):
                if root is None:
                    return
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)

            def construct(arr):
                if not arr:
                    return None
                mid = len(arr) // 2
                root = TreeNode(arr[mid])
                root.left = construct(arr[:mid])
                root.right = construct(arr[mid+1:])
                return root
            
            inorder(root)
            return construct(arr)
        
        root = balanceBST(root)
        output = []
        for query in queries:
            self.low = self.big = -1
            self.traverse(root, query)
            output.append([self.low, self.big])
        return output