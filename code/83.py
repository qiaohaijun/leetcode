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
        mockHead = ListNode(-1)
        # save the return value for linked list
        mockHead.next = head
        # the loop head
        preHead = mockHead
        preHead = preHead.next
        #1->1->1->1
        # 相同的时候，只管删除
        # 不相同的时候，才要移动指针
        while preHead.next is not None:

            if preHead.next.val == preHead.val:
                print preHead.val
                print preHead.next.val
                preHead.next = preHead.next.next
            else:
                preHead = preHead.next
                
        return mockHead.next
        
            
        
        
