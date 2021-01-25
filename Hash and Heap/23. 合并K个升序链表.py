# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1.两两合并
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        listsLen = len(lists)
        res = []
        def mergeTwoLists(head1, head2):
            temp = ListNode(0)
            head = temp
            while head1 != None and head2!=None:
                if head1.val < head2.val:
                    temp.next = head1
                    temp = temp.next
                    head1 = head1.next
                else:
                    temp.next = head2
                    temp = temp.next
                    head2 = head2.next
            while head1 != None:
                temp.next = head1
                temp = temp.next
                head1 = head1.next
            while head2 != None:
                temp.next = head2
                temp = temp.next
                head2 = head2.next
            return head.next
        while listsLen > 1:
            i = 0
            while i < listsLen - 1:
                res.append(mergeTwoLists(lists[i], lists[i + 1]))
                i += 2
            if i == listsLen - 1:
                res.append(lists[i])
            lists = res
            res = []
            listsLen = len(lists)
        return lists[0]



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#2.分治法
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        listsLen = len(lists)
        res = []
        def mergeTwoLists(head1, head2):
            temp = ListNode(0)
            head = temp
            while head1 != None and head2!=None:
                if head1.val < head2.val:
                    temp.next = head1
                    temp = temp.next
                    head1 = head1.next
                else:
                    temp.next = head2
                    temp = temp.next
                    head2 = head2.next
            while head1 != None:
                temp.next = head1
                temp = temp.next
                head1 = head1.next
            while head2 != None:
                temp.next = head2
                temp = temp.next
                head2 = head2.next
            return head.next
        def Merge(lists, start, end):
            if not lists:
                return None
            if end - start == 0:
                return lists[start]
            if end - start == 1:
                return mergeTwoLists(lists[start], lists[end])
            mid = start + (end - start) // 2
            left = Merge(lists, start, mid)
            right = Merge(lists, mid + 1, end)
            return mergeTwoLists(left, right)
        return Merge(lists, 0, listsLen - 1)
            


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#3.优先队列
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        heap = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        while heap:
            val = heapq.heappop(heap)
            point.next = ListNode(val)
            point = point.next
        return head.next

        
            