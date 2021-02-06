# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#1.递归
class Solution:
    def helper(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
        return False
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)

#2.迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, left, right):
        queue = []
        queue.append(left)
        queue.append(right)
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if (not left or not right) or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check(root, root)
        
