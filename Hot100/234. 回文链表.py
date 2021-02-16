# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node = slow.next
        slow.next = None
        secondHead = self.reverseList(node)
        while head and secondHead:
            if head.val != secondHead.val:
                return False
            head = head.next
            secondHead = secondHead.next
        return True
  
    def reverseList(self, head):
        if not head:
            return None
        pre = head
        cur = head.next
        pre.next = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre





