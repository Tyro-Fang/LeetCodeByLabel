# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 队列迭代法 
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        tempRes = []
        while queue:
            temp = []
            for i in range(len(queue)):
                n = queue.pop(0)
                temp.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            tempRes.append(temp)
        res = []
        while tempRes:
            res.append(tempRes.pop())
        return res 

#递归
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root,depth):
            if not root:
                return []
            if len(res) < depth + 1:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left,depth + 1)
            dfs(root.right,depth + 1)
        dfs(root,0)
        return res[::-1]