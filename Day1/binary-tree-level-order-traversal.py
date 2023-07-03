# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lvls = {}

    def helper(self, root, lvl):
        if root is None:
            return
        self.helper(root.left, lvl+1)
        if lvl in self.lvls:
            self.lvls[lvl].append(root.val)
        else:
            self.lvls[lvl] = [root.val]
        self.helper(root.right, lvl+1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.helper(root, 0)
        lvl = 0
        output = []
        while 1:
            if lvl in self.lvls:
                output.append(self.lvls[lvl])
            else:
                break
            lvl += 1
        return output