# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return None
        max1, max2 =  self.helper(root)
        return max(max1, max2)


    def helper(self, root):
        if not root.left and not root.right:
            return root.val, root.val
        leftMax = rightMax = leftAllMax = rightAllMax = -sys.maxsize - 1
        if root.left:
            leftMax, leftAllMax = self.helper(root.left)
        if root.right:
            rightMax, rightAllMax = self.helper(root.right)
        allMax = max(leftAllMax, rightAllMax)
        return max(max(leftMax, rightMax) + root.val, root.val), max(allMax, max(max(leftMax, 0) + max(rightMax, 0) + root.val, root.val))
        
        
        