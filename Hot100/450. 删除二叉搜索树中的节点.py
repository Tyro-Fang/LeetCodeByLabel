# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root or key == None:
            return root
        dummy = TreeNode(sys.maxsize)
        dummy.left = root
        self.dfs(dummy, key)
        return dummy.left
        
    def dfs(self, root, key):
        if not root:
            return
        if key > root.val:
            if root.right:
                if root.right.val == key:
                    root.right = self.deleteOneNode(root, root.right)
                    return
                else:
                    self.dfs(root.right, key)
        else:
            if root.left:
                if root.left.val == key:
                    root.left = self.deleteOneNode(root, root.left)
                    return
                else:
                    self.dfs(root.left, key)
        


    def deleteOneNode(self, root, delNode):
        left = delNode.left
        right = delNode.right
        if not left and not right:
            return None
        elif not left:
            return right
        elif not right:
            return left
        else:
            rightCache = right.left
            if not rightCache:
                right.left = left
                
            else:
                self.addNode(right, left)
            return right

    def addNode(self, root, addNode):
        if not root.left:
            root.left = addNode
            return
        self.addNode(root.left, addNode)
