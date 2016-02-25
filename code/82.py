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
        #----------------------------------------------------------
        if head is None or head.next is None:
            return head
        #----------------------------------------------------------    
        
        table = dict()
       
        #----------------------------------------------------------
        mockHead = ListNode(-1)
        mockHead.next = head
        preHead = mockHead
        #-----------------------------------------------------------
        
        while preHead.next is not None:
            if table.has_key(preHead.next.val):
                table[preHead.next.val] = table[preHead.next.val]+1
            else:
                table[preHead.next.val] = 0
            preHead = preHead.next
        
        print table
        
        #-------------------------------------------------------------
        
        preHead = mockHead
        
        while preHead.next is not None:
            if table[preHead.next.val] > 0:
                preHead.next = preHead.next.next
            else:
                preHead = preHead.next
                
        #--------------------------------------------------------------
        
        return mockHead.next
        
