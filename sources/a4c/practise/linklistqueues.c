#include<stdio.h>
#include<stdlib.h>


typedef struct node{
    int val;
    node *next;
    node *prev;
}node;
node *temp;
node *temp2;
node*head;
node *tail;
int t=0;
void add(int i){

    node *trs=(node*)malloc(sizeof(node));
    if (t==0){
        head=trs;
        head->prev=NULL;
        t++;

    }else{
        temp->next=trs;
        trs->prev=temp;
    }
    temp=trs;
    printf(":");
    scanf("%d",&trs->val);
    if (i==5){
        tail=trs;
        trs->next=NULL;
    }
    

}
// void reverse(){
//     temp2=head;
// while(temp2!=NULL){
//     temp=temp2->prev;
//     temp2->prev=temp2->next;
//     temp2->next=temp;
//     temp2=temp2->prev;
// }
// if(temp != NULL){
//         head = temp->prev;
//     }
// while(temp2!=NULL){
//         printf("%d ",temp2->val);
//         temp2=temp2->next;
//     }
// }

void print(){
    while(head!=NULL){
        printf("%d ",head->val);
        head=head->next;
    }
}

int main(){
for(int i =0;i<6;i++){
add(i);
}

print();
// reverse();


system("pause");
return 0;
}