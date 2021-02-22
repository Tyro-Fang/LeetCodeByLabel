# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, root):
        if not root:
            return None
        temp = root.right
        if root.left:
            root.right = root.left
            root.left = None
            endNode = self.helper(root.right)
            if endNode:
                endNode.right = temp
            return temp
        else:
            return root.right

