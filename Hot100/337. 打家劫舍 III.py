# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        maxVals = self.dfs(root)
        return max(maxVals[0], maxVals[1])

    def dfs(self, root):
        if not root:
            #0位表示没选择子节点的最大值，1位表示选择子节点的最大值
            return[0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return [max(left[0],left[1]) + max(right[0], right[1]), left[0] + right[0] + root.val]
        