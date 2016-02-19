# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # pre condition
        if head is None or head.next is None:
            return head
            
        uniqSet = set()
        dummy=ListNode(0)
        dummy.next = head
        
        while  dummy is not None and dummy.next is not None:
            if dummy.next.val in uniqSet:
                dummy.next = dummy.next.next
            else:
                uniqSet.add(dummy.next.val)
                
            dummy = dummy.next
            print uniqSet
        
        return dummy
