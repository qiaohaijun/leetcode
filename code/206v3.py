# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
 def reverseList(self, head):
    if not head or not head.next:
        return head
    ret = None
    while head:
        tmp = head
        head = head.next
        tmp.next = ret
        ret = tmp
    return ret

            
        
