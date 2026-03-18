#include <stdio.h>
#include <stdlib.h>
int max;
int rear=-1;
int front;

void push(int s1[],int value){
    s1[rear]=value;
    rear++;
}
void move(int s1[],int s2[],int size){
    int j=0;
    for (int i =size ;i>0;i--){
        s2[j]=s1[i];
        j++;
        front++;
        rear=0;
    }

}
void pop(int s1[],int s2[],int size){
  move(s1,s2,size);
  return s2[front];
  front--;
}

void isempty(int s2[],int s1,int size){
    if(front+rear==0){
        printf("empty");
        return;
    }
    printf("not empty");
}


void top(){



}

int main(){
    int n;
    printf("size of queue?");
    scanf("%d",&n);
    max=n;
    
    


    system("pause");
    return 0;
}