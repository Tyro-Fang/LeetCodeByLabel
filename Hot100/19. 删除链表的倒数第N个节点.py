# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        dommy = ListNode(0)
        dommy.next = head
        slowPtr = fastPtr = dommy
        for i in range(n):
            if fastPtr.next == None:
                break
            fastPtr = fastPtr.next
        while fastPtr:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
        slowPtr.next = slowPtr.next.next
        return dommy.next