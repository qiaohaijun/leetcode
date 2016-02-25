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
        
        pre = head
        mid = head.next
        last = head.next.next
        
        #----------------------------------------
        
        mid.next = pre
        pre.next = None
        pre = mid
        mid = last

        while last is not None:
            last = last.next
            mid.next = pre
            pre = mid
            mid = last
            
            
        #-----------------------------------------
        

        return pre
        
            
        
