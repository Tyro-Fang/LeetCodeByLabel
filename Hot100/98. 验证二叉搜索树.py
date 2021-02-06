# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -sys.maxsize - 1
    def helper(self, root):
        global pre
        if not root:
            return True
        if not self.helper(root.left):
            return False
        if root.val <= pre:
            return False
        pre = root.val
        return self.helper(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        global pre
        pre = -sys.maxsize - 1
        if not root:
            return False
        return self.helper(root)
