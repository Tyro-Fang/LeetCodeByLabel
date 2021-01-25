# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        def twoMerge(head1, head2):
            dummy = head = ListNode(0)
            while head1 or head2:
                if not head1:
                    head.next = head2
                    break
                if not head2:
                    head.next = head1
                    break
                if head1.val < head2.val:
                    head.next = head1
                    head1 = head1.next
                else:
                    head.next = head2
                    head2 = head2.next
                head = head.next
            return dummy.next
        res = []
        while len(lists) > 1:
            allLen = len(lists)
            i = 0
            while i + 1 < allLen:
                res.append(twoMerge(lists[i], lists[i + 1]))
                i += 2
            if i == allLen - 1:
                res.append(lists[i]) 
            lists = res
            res = []
        return lists[0]
                


                

        