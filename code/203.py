# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
// 如果不使用dummy node，很难删除自己
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return
        print head.val
        dummy = ListNode(0)
        dummy.next = head;
        ret = dummy
        
        while dummy.next is not None:
            if val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return ret.next
                
