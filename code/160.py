# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

// 这个题目需要注意的是，是否有环
// 我这个题目用的方法是对链表做了两次遍历，然后大家从同一个起点开始
// 空间复杂的是O(1)
// 如果可以使用dict的话，那个这个问题就好办了，但是空间复杂度是O(n)
// 但是代码会简单很多
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
        
         
