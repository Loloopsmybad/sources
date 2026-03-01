#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int value;
    int address;
}NODE;

void allocate_mem(int *n){

NODE * linkedlist=(NODE*)malloc((*n)*sizeof(NODE));

}

int main(){
    int n=0;
    printf("no of node required ?");
    scanf("%d", &n);


    system("pause");
    return 0;
}