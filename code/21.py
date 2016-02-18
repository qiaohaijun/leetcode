# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 这个题目的边界条件
# l1 or l2 其中一个
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        
        dummy = ListNode(0);
        retList = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1=l1.next
            else:
                dummy.next = l2
                dummy = dummy.next
                l2=l2.next
        while l1 is not None:
            dummy.next = l1
            dummy = dummy.next
            l1 = l1.next
        while l2 is not None:
            dummy.next = l2
            dummy = dummy.next
            l2 = l2.next
            
        return retList.next
