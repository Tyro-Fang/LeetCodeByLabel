# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return root
        preData = self.preOrder(root)
        return preData 
        

    def preOrder(self, root):
        if not root:
            return 'X'
        left = self.preOrder(root.left)
        right = self.preOrder(root.right)
        return str(root.val) + ',' + left + ',' + right

    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        listData = data.split(',')
        return self.restoreTree(listData)
    
    def restoreTree(self, data):
        if not data:
            return None
        val = data.pop(0)
        if val == 'X':
            return None
        root = TreeNode(val)
        left = self.restoreTree(data)
        right = self.restoreTree(data)
        root.left = left
        root.right = right
        return root
    

