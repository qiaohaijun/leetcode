# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
             return head
        #help node
        
        helper = ListNode(None)
        pre = helper
        cur = head
        
        while cur is not None:
            # 保存下一个节点的状态
            next = cur.next
            pre = helper
            while pre.next is not None and pre.next.val <= cur.val:
                pre = pre.next
                #print pre.val
            
            cur.next = pre.next
            pre.next = cur
            cur = next
            
        return helper.next
            
            
