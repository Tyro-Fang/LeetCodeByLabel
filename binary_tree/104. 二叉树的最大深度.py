# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countDepth(root, 0)

    def countDepth(self, root, depth):
        if not root:
            return depth
        depth += 1
        leftDepth, rightDepth = depth, depth
        if root.left != None:
            leftDepth = self.countDepth(root.left, depth)
        if root.right != None:
            rightDepth = self.countDepth(root.right, depth)
        return max(leftDepth, rightDepth)
    