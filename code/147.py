# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
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
            # trick 只有当当前的节点小于已经排好序的节点的位置的时候，然后重置位置
            if cur.val < pre.val:
                pre = helper
            while pre.next is not None and pre.next.val <= cur.val:
                pre = pre.next
                #print pre.val
            
            cur.next = pre.next
            pre.next = cur
            cur = next
            
        return helper.next
