# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.dfs(root, res)
        return res
    
    def dfs(self, root, res):
        if not root:
            return 0
        leftDepth = self.dfs(root.left, res)
        rightDepth = self.dfs(root.right, res)
        curDepth = max(leftDepth, rightDepth) + 1
        if len(res) < curDepth:
            res.append([])
        res[curDepth - 1].append(root.val)
        return curDepth