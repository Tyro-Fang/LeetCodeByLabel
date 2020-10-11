# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            queueLength = len(queue)
            for i in range(queueLength):
                n = queue.pop(0)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
                if i == queueLength - 1:
                    res.append(n.val)
        return res