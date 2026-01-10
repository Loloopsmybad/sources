

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;
    struct ListNode *compansate;
    struct ListNode *compansate2;
    struct ListNode *head;
    int i,a,b=0;

    while (list1->next!=NULL){
        if (i <1){
            head=list1;
        }
        
            if ((list2->val) >= (list1->val)){
                compansate=list1->next;
                compansate2=list2->next;
                list1->next=list2;
                list2->next=compansate;
                list1=list2->next;
                list2=compansate2;
            }
            
            else if((list2->val) <= (list1->val)){
                compansate=list1->next;
                compansate2=list2->next;
                list1->next=list2;
                list2->next=compansate;
                a=list1->val;
                b=list2->val;
                list1->val=b;
                list2->val=a;
                list1=list2->next;
                list2=compansate2;

            }
        i++;
        }
        if (i <1){
            head=list1;
        }
        if ((list2->val) >= (list1->val)){
                compansate=list1->next;
                compansate2=list2->next;
                list1->next=list2;
                list2->next=compansate;
                list1=list2->next;
                list2=compansate2;

            }
            
        else if((list2->val) < (list1->val)){
                compansate=list1->next;
                compansate2=list2->next;
                list1->next=list2;
                list2->next=compansate;
                a=list1->val;
                b=list2->val;
                list1->val=b;
                list2->val=a;
                list1=list2->next;
                list2=compansate2;
                
        }


    return head;

}
