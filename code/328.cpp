
 // Definition for singly-linked list.
/*
[NULL] 边界条件
[1]  边界条件
[1,2,3,4] 正常case
*/

class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        // 注意边界条件
        if(NULL==head || NULL==head->next||NULL==head->next->next) {
            return head;
        }
        ListNode * odd = head;
        ListNode * even = head->next;
        // 需要保存两个链表的head
        // first
        // second
        ListNode * second = even;
        ListNode * first = odd;

        head = head->next->next;
   
        int count = 1;
        //非常容易读的code
        while(head!=NULL) {
            if(count %2 ==1) {
                odd->next = head;
                odd=odd->next;
            } else {
                even->next = head;
                even = even->next;
            }
            head = head->next;
            count++;
        }
        odd->next = second;
        even->next =NULL;
        return first;

    }
};
