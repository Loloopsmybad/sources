#include<stdio.h>
#include<stdlib.h>

typedef struct Node
{
    int val;
    Node * next;
}Node;


Node *head;
Node *temp;
int c=0;
void printall(){
    while (head!=NULL){
            printf("value : %d \n",head->val);
            head=head->next;
        }
}

void add(){
    int a;
    for(;;){
    Node * link=(Node *)malloc(sizeof(Node));
    if (c!=1){
        head=link;
        c++;
    }else{
        temp->next=link;
    }
    printf("\n======================================\n");
    printf("value fot the current node ?");
    scanf("%d",&link->val);
    temp=link;
    printf("\n======================================\n");


    printf("do you want to add another a node '1' or  print all thhe nodes '2'?");
    scanf("%d",&a);

    if (a==1){
        continue;
    }else if (a==2){
        link->next=NULL;
        printall();
        break;
    }else{
        link->next=NULL;
        break;
    }
    }
    
}



int main(){
    add();
    system("pause");
    return 0;
}