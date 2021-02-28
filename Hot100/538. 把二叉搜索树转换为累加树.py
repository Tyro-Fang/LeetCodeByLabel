# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    global ans
    def convertBST(self, root: TreeNode) -> TreeNode:
        global ans
        ans = 0
        self.traverseTree(root)
        return root
    
    def traverseTree(self, root):
        global ans
        if not root:
            return
        self.traverseTree(root.right)
        ans += root.val
        root.val = ans
        self.traverseTree(root.left)
        


    