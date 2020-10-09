class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        nodeStack = []
        pNode = root
        while pNode !=None or nodeStack != []:
            while pNode != None:
                nodeStack.append(pNode)
                pNode = pNode.left
            pNode = nodeStack.pop()
            result.append(pNode.val)
            pNode = pNode.right
        return result