# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#1.reverse
class Solution:
    def helper(self, root, res):
        if not root:
            return 
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res


#2.stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        while root or stack:
            while root :
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

