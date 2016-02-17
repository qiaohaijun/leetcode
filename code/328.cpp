
 // Definition for singly-linked list.


class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {

        if(NULL==head || NULL==head->next||NULL==head->next->next) {
            return head;
        }
        ListNode * odd = head;
        ListNode * even = head->next;
        ListNode * second = even;
        ListNode * first = odd;

        head = head->next->next;
   
        int count = 3;
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
