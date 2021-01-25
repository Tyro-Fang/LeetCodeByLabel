# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        pNode = head
        listLength = 0
        while pNode != None:
            listLength += 1
            pNode = pNode.next
        def dfs(headNode, length):
            if not headNode:
                return None
            if length == 1:
                res = TreeNode(headNode.val)
                return res
            middle = length // 2
            startNode = headNode
            prev, curr = None, headNode
            for _ in range(middle):
                prev = curr 
                curr = curr.next
            prev.next = None
            res = TreeNode(curr.val)
            res.left = dfs(startNode, middle)
            res.right = dfs(curr.next, length - middle - 1)
            return res
        return dfs(head, listLength)
