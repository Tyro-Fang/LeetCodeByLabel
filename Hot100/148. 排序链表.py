# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#1.非常数空间复杂度
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        ptr = head
        tempRes = []
        while ptr:
            tempRes.append(ptr.val)
            ptr = ptr.next
        tempRes.sort()
        ptr = head
        i = 0
        while ptr:
            ptr.val = tempRes[i]
            i += 1
            ptr =ptr.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        right = slow.next
        slow.next = None
        leftResult = self.sortList(head)
        rightResult = self.sortList(right)
        ptr = dummy = ListNode(0)
        while leftResult or rightResult:
            if not leftResult:
                ptr.next = rightResult
                break
            if not rightResult:
                ptr.next = leftResult
                break
            if leftResult.val < rightResult.val:
                ptr.next = leftResult
                leftResult = leftResult.next
            else:
                ptr.next = rightResult
                rightResult = rightResult.next
            ptr = ptr.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        invite = 1
        while True:
            ptr = head
            while ptr:
                nextPtr = ptr
                for _ in range(invite):
                    nextPtr = nextPtr.next
                    if not nextPtr:
                        return head
                first = ptr
                temp = []
                for _ in range(2 * invite):
                    if nextPtr.val < ptr.val:
                        temp.append(nextPtr.val)
                        nextPtr = nextPtr.next
                    else:
                        temp.append(ptr.val)
                        ptr = ptr.next
                for _ in range(2 * invite):
                    first.val = temp.pop(0) 
                    first = first.next   
                ptr = first
            invite *= 2    

            
                    
a = ListNode(4)
b = ListNode(2)
c = ListNode(1)
d = ListNode(3)
a.next = b
b.next = c
c.next = d
x = Solution2()
x.sortList(a)

