# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def pathSum(self, root: TreeNode, sum: int) -> int:
        global count
        count = 0
        if not root or sum == None:
            return 0
        self.dfs(root, [], sum)
        return count
    def dfs(self, root, vals, target):
        global count
        if not root:
            return 
        if root.val == target:
            count += 1
        tempVals = []
        for i in vals:
            if i + root.val ==  target:
                count += 1
            tempVals.append(i + root.val)
        tempVals.append(root.val)
        self.dfs(root.left, tempVals, target)
        self.dfs(root.right, tempVals, target)