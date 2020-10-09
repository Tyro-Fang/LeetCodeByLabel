# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        return self.helper(root)

    def helper(self, root):
        if not root:
            return None
        left = self.helper(root.left)
        right = self.helper(root.right)
        root.right = left
        root.left = right
        return root