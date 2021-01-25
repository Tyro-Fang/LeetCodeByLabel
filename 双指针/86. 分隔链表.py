# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        smallNodes = ListNode(0)
        bigNodes = ListNode(0)
        res = smallNodes
        temp = bigNodes
        while head != None:
            if head.val < x:
                smallNodes.next = head
                head = head.next
                smallNodes = smallNodes.next
                smallNodes.next = None
            else:
                bigNodes.next = head
                head = head.next
                bigNodes = bigNodes.next
                bigNodes.next = None
        smallNodes.next = temp.next
        
        return res.next

