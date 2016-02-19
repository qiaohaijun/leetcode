# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 位数是否相同
# 倒序
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # [None]
        # [None]
        if l1 is None and l2 is None:
            return None
        
        dummy = ListNode(0)
        retList = dummy
        up = 0
        
        # 处理正常的情况
        while l1 is not None and l2 is not None:
            # print (l1.val+l2.val+up)%10
            dummy.next = ListNode((l1.val+l2.val+up)%10)
            up = (l1.val+l2.val+up)/10
            
            # print "up",up
            # print "l1.val", l1.val
            # print "l2.val", l2.val
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
            
        # [1,2]
        # [1]
        while l1 is not None:
            dummy.next = ListNode((l1.val+up)%10)
            up=(l1.val+up)/10
            dummy = dummy.next
            l1 = l1.next
            
        # [1]
        # [1,2]
        while l2 is not None:
            dummy.next = ListNode((l2.val+up)%10)
            up=(l2.val+up)/10
            dummy = dummy.next
            l2 = l2.next
        
        #处理最后的还有一个进位的情况
        # [5]
        # [5]
        if up>0:
            dummy.next = ListNode(up)
        return retList.next
