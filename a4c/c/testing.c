#include <stdio.h>
#include <stdlib.h>

struct NODE {
        int value;
        struct NODE *next;
};

void linkedlist(struct NODE* address) {
    while (address != NULL) {
        printf("%d\n", address->value);//same as (*address).value
        address = address->next;
    }
}

int main(){
        printf("fuck you ");
        struct NODE head;
        struct NODE second;
        head.value=1;
        head.next= &second;
        second.value=2;
        second.next=NULL;
        linkedlist(&head);
        system("pause");
        return 0;
}