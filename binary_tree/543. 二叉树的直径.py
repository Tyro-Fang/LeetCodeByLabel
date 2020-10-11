# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    ans = 1
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        global ans
        if not root:
            return 0
        return ans
    
    def helper(self, root):
        global ans
        if not root:
            return  0
        left = self.helper(root.left)
        right = self.helper(root.right)
        ans = max(ans,left + right + 1)
        return max(left, right) + 1

#类似BFS
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        def depth(root):
            if not root:
                return 0
            queue=[root]
            height = 0
            while queue:
                height += 1
                for i in range(len(queue)):
                    n=queue.pop(0)
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
            return height
        queue=[root]
        res = 0
        while queue:
            n = queue.pop(0)
            res = max(res, depth(n.left) + depth(n.right))
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)
        return res
            




        
        
    
        
