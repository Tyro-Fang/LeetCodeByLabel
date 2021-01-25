# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        def dfs(root):
            start = root
            if root.left == None and root.right == None:
                return root
            if root.left != None:
                endNode = dfs(root.left)
                if root.right != None:
                    rightTemp = root.right
                    root.right = root.left
                    endNode.right = rightTemp
                    endNode = dfs(rightTemp)
                else:
                    root.right = root.left
                root.left = None
                return endNode
            else:
                endNode = dfs(root.right)
                return endNode
        dfs(root)    
                    

