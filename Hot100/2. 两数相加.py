# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return None
        res = []
        carryBit = 0

        while l1 != None or l2 != None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carryBit
            carryBit, total = divmod(total, 10)
            res.append(total)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carryBit == 1:
            res.append(1)
        head = ListNode()
        ptr = head
        for _, v in enumerate(res):
            temp = ListNode(v)
            ptr.next = temp
            ptr = ptr.next
        return head.next
        




