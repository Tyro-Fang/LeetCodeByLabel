# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        ptrA = headA
        ptrB = headB
        while ptrA and ptrB:
            ptrA = ptrA.next
            ptrB = ptrB.next
        if not ptrA:
            ptrA = headB
            while ptrB:
                ptrB = ptrB.next
                ptrA = ptrA.next
            ptrB = ptrA
            ptrA = headA
             
        else:
            ptrB = headA
            while ptrA:
                ptrA = ptrA.next
                ptrB = ptrB.next
            ptrA = ptrB
            ptrB = headB
        while ptrB != ptrA:
            ptrB = ptrB.next
            ptrA = ptrA.next
        if ptrA == None:
            return None
        else:
            return ptrA
        
