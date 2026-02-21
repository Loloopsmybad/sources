#include<stdio.h>
#include<stdlib.h>
int ar[5];
int front= -1;
int rear = -1;
void print(){
    for (int i=0;i<5;i++){
        printf("|%d",ar[i]);
    }
    printf("\n");
}

void enqueue(int a){
    if((rear+1)%5==front){//checks if there is space in the beginning
        printf("queue full\n");
        return;
    }
    if(front== -1){
        front=rear=0;
    }
    else{
        rear=(rear+1)%5;
    }
    ar[rear]=a;
    printf("rear:%d\n",rear);
    print();

}

void dequeue(){
    if (front== -1){
        printf("queue empty");
        return;
    }
    if(front==rear){
        printf("hi");
        front=rear=-1;//only possible when all lements are removed
    }
    ar[front]=0;
    front=(front+1)%5;
    printf("front:%d\n",front);
    printf("dequeue\n");
    print();
}

int main(){
    enqueue(10);
    enqueue(1);
    enqueue(44);
    dequeue();
    enqueue(44);
    enqueue(44);
    enqueue(44);
    dequeue();
    dequeue();
    enqueue(44);
    enqueue(4);
    system("pause");
    return 0;
}