#include <stdlib.h>
#include<stdio.h>


struct NODE{ 
    int val;
    struct NODE *next;
};


int main(){

    struct NODE *head = (struct NODE *)malloc(sizeof(struct NODE));

    head->val=1;
    head->next=NULL;
    printf("%d",head->val);
    system("pause");


}