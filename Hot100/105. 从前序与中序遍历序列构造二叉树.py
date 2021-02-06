# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        return self.build(preorder,0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, p_left, p_right, inorder, i_left, i_right):
        if p_left > p_right:
            return None
        root = TreeNode(preorder[p_left])
        i = 0
        while i <= (i_right - i_left + 1):
            if inorder[i_left + i] == preorder[p_left]:
                break
            i += 1
        root.left = self.build(preorder, p_left + 1, p_left +  i, inorder, i_left, i_left + i - 1)
        root.right = self.build(preorder,p_left + i + 1, p_right, inorder, i_left + i + 1, i_right)
        return root
