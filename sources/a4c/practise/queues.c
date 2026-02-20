#include<stdio.h>
#include<stdlib.h>


typedef struct node{
    int val;
    node *next;
    node *prev;
}node;
node *temp;
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

void print(){
    while(tail!=NULL){
        printf("%d ",tail->val);
        tail=tail->prev;
    }
}

int main(){
for(int i =0;i<6;i++){
add(i);
}
print();

system("pause");
return 0;
}