#include <stdlib.h>
#include<stdio.h>

// lesson learned

// for doubly linked list or
//forr merging two linked lists 
// u require address to next node prev node  and value that u want to store

struct ListNode {
    int val;
    struct ListNode *next
};

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;

 
}
