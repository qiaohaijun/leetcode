# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
            
        lenA = 0
        lenB = 0
        tmpA = headA
        tmpB = headB
        longList = None
        shortList = None
        while tmpA is not None:
            lenA +=1
            tmpA = tmpA.next
        
        while tmpB is not None:
            lenB +=1
            tmpB = tmpB.next
        
        if lenA >= lenB:
            longList = headA
            shortList = headB
        else:
            longList = headB
            shortList = headA
        
        dist = abs(lenA-lenB)
        print dist
        
        while dist > 0:
            longList = longList.next
            print "b"
            dist -= 1
        
        while longList is not None:
            if longList == shortList:
                return longList
            longList = longList.next
            shortList = shortList.next
        return None
        
         
