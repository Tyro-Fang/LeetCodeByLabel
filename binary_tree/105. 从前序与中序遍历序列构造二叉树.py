# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        return self.helper(preorder, inorder)

    def helper(self, preorder, inorder):
        if len(preorder) != len(inorder) or len (preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        index, target = -1, preorder[0]
        for i in range(len(inorder)):
            if inorder[i] ==  target:
                index = i
                break
        if index != -1:
            root.left = self.helper(preorder[1:index+1], inorder[:index])
            root.right = self.helper(preorder[index+1:], inorder[index+1:])
            return root
        else:
            return None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def helper(self, preorder, prestart, preend, inorder, instart, inend):
        if len(preorder) != len(inorder) or len (preorder) == 0:
            return None
        if prestart > preend :
            return None
        root = TreeNode(preorder[prestart])
        inorder_root = index[preorder[prestart]]
        leftTreeLenght = inorder_root - instart
        root.left = self.helper(preorder, prestart + 1,prestart + leftTreeLenght, inorder, instart, inorder_root -1)
        root.right = self.helper(preorder, prestart + leftTreeLenght + 1, preend, inorder, inorder_root + 1, inend)
        return root
        