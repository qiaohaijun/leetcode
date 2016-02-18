/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 //考点
 //不是常规的删除节点操作，如果是常规的操作，会直接将父指针修改，这个题目没有给出父指针
 // 所以这个是一个变通的题目
class Solution {
public:
    void deleteNode(ListNode* node) {
    // 删除的是val 和 post 一样的
    // index from 0
// 1. NULL==node 判断是否是一个NULL操作，也就是不删除任何节点
// 2. NULL==node->next 判断是否给的node是最后一个节点，也就是题目中的tail node
        if(NULL==node || NULL==node->next)
        {
            return ;
        }
        
        node->val = node->next->val;  
        node->next = node->next->next;  
    
        
    }
};
