# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.divideAndConquer(lists)
        
    def divideAndConquer(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = (len(lists)-1) // 2
            leftList = self. divideAndConquer(lists[0:mid+1])
            rightList = self.divideAndConquer(lists[mid+1:])
            return self.mergeTwoLists(leftList, rightList)

    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        pNode1 = list1
        pNode2 = list2
        headNode = None
        result = None
        while pNode1 and pNode2:
            if pNode1.val < pNode2.val:
                tempNode = pNode1
                pNode1 = pNode1.next
            else:
                tempNode = pNode2
                pNode2 = pNode2.next
            if headNode == None:
                headNode = tempNode
                result = headNode
            else:
                headNode.next = tempNode
                headNode = headNode.next
        if pNode1 == None:
            headNode.next = pNode2
        elif pNode2 == None:
            headNode.next = pNode1
        return result
                  
            