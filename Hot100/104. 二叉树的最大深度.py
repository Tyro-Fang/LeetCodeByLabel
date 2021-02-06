# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.findDepth(root, 0)
        
    def findDepth(self, root, depth):
        if not root:
            return depth
        depth += 1
        return max(self.findDepth(root.left, depth), self.findDepth(root.right, depth))