# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def dfs(rootOne, rootTwo):
            if rootOne == rootTwo == None:
                return True
            elif rootOne == None:
                return False
            elif rootTwo == None:
                return False
            elif rootOne.val == rootTwo.val:
                return dfs(rootOne.left, rootTwo.right) and dfs(rootOne.right, rootTwo.left)
            else:
                return False
        return dfs(root.left, root.right)

