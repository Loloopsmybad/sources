#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>



int *s1;
int *s2;
int top1 = -1;
int top2 = -1;
int max_size;
int choice;
int val;



void push(int arr[], int *top, int value){
    (*top)++;
    arr[*top] = value;
    
}


int pop(int arr[], int *top){
    int x =arr[*top];
    (*top)--;
    return x;
    
}

int top(int arr[], int t){
    return arr[t];
}

int isEmpty(int t){
    if (t==-1){
        return true;
    }
    return false;
}


int size(){
    int x =(top1 + 1) + (top2 + 1);
    return x;
}

int isqueueEmpty(){
    if (isEmpty(top1)== true && isEmpty(top2)==true){
        return true;
    }
    return false;
}


int isunderflow(){
    if (isqueueEmpty()==true) {
        printf("queue is empty\n");
        return true;
    }
    return false;
}

int isoverflow(){
    if (size() == max_size) {
        printf("queue is full\n");
        return true;
    }
    return false;

}

void move() {
    while (isEmpty(top1)==false) {
        int x = pop(s1,&top1);
        push(s2,&top2,x);
    }

}


void enqueue(int val){
    if (isoverflow()==true){
       return;
    }
    push(s1, &top1, val);
    printf("enqueued: %d s1 size = %d  s2 size = %d \n", val, top1+1, top2+1);

}

int dequeue(){
    if (isunderflow()==true){
        return 0;
    }
    if (isEmpty(top2)==true){
        move();
    }
    int val = pop(s2,&top2);
    return val;
}

int front(){
    if (isunderflow()==true){
        return 0;
    }
    if (isEmpty(top2)==true){
        move();
    }
    int value = top(s2, top2);
    return value;
}
void choice_a(){
    if (choice==1){
                printf("Enter number to enqueue--> ");
                scanf("%d", &val);
                enqueue(val);
                printf("\n");
                
    }else if (choice==2){
        int x =dequeue();
        printf("dequeued--> %d  s1 size = %d  s2 size = %d \n", x,top1+1,top2+1);
    }else if (choice==3){
            printf("front-->%d \n", front());
    }else if (choice==4){
            printf("size of the quque is --> %d \n", size());
    }
    else if (choice==5){
            return;        
    }
}
int main() {
    printf("enter the size of queue ?-->");
    scanf("%d", &max_size);

    s1 = (int *)malloc(max_size * sizeof(int));
    s2 = (int *)malloc(max_size * sizeof(int));
    
    printf("enqueue-->1 ,dequeue-->2  front-->3  size of queue-->4 ");
    scanf("%d", &choice);
    while (true){
        choice_a();
        if(choice==5){
            break;
        }
        printf("enqueue-->1 ,dequeue-->2  front-->3  size of queue-->4 ");
        scanf("%d", &choice);
    }
    system("pause");
    return 0;
}