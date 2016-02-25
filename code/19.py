# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#[] None
#[1] one
#[1,2,3] normal
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None :
            return head
        if n <=0:
            return head
            
        #------------------------------------
        print n
        mockHead = ListNode(-1)
        mockHead.next = head
        
        #-------------------------------------
        firstHead = mockHead
        
        while n > 0:
            firstHead = firstHead.next
            n=n-1
        
        secondHead = mockHead
        
        while firstHead.next is not None:
            firstHead = firstHead.next
            secondHead = secondHead.next
        
        
        #--------------------------------
        
        secondHead.next = secondHead.next.next
        
        return mockHead.next
