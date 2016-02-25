# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #---------------------------------------
        
        if head is None or head.next is None:
            return head
        #---------------------------------------
        
        mockHead = ListNode(-1)
        mockHead.next = head
        pre = mockHead
        mid = mockHead.next
        last = mockHead.next.next
        
        #----------------------------------------
        #---------------------------------------

        while last.next is not None:
            mid.next = pre
            
            pre = mid
            mid = last
            last = last.next

            
            
        #-----------------------------------------
        last.next = mid

        return last
        
            
        
