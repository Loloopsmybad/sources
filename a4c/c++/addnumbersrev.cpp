/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int a=0;
        int b=0;
        int c=0;
        int d =0;
        ListNode* l3;
        ListNode* header;
        while (l1!=NULL){
            a=(a*10)+l1->val;
            l1=l1->next;
        }
        while (l2!=NULL){
            b=(b*10)+l2->val;
            l2=l2->next;
        }
        while (a!=0){
            c=(c*10)+(a%10);
            a=a/10;
        }
        a=c;
        c=0;
        while (b!=0){
            c=c*10+b%10;
            // cout<<c;
            b=b/10;
        }
        b=c;
        c=a+b;
        while(c!=0){
            ListNode* a =new ListNode();
            a->val=c%10;
            if (d==0){
                l3=a;
                header =a;
            }else{
                l3->next=a;
                l3=a;
            }
            d++;
            c/=10;

        }
        return header; 
    }
     
};