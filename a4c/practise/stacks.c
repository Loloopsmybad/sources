#include<stdio.h>
#include<stdlib.h>

int n;
void push(int *a ,int *top,int val){
    if ((*top)>=n){
        printf("overflown");
        return;
    }
    
    a[(*top)]=val;
    (*top)++;
    
}
int pop(int *a,int *top){
    if ((*top)==0){
        printf("UNDERflown");
        return 99;
    }
    top--;
    
    return a[(*top)+1];
}
void print(int*a,int *top){
    for (int i = 0;i<(*top);i++){
        printf("%d \n",a[i]);
    }
}

int main(){
int top=0;
n=4;

int *a =(int*)malloc(n*sizeof(int));

push(a,&top,5);
printf("\n");
push(a,&top,4);
printf("\n");
push(a,&top,3);
printf("\n");
push(a,&top,2);
printf("\n");
print(a,&top);

printf("%d",top);
system("pause");
return 0;
}