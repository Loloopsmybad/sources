#include<stdlib.h>
#include<stdio.h>


void insertionsort(int *a,int size){
for (int i=1;i<size;i++){
    int key=a[i];
    int j =i-1;
    while(j>-1 && a[j]>key){
        a[j+1]=a[j];
        j--;
    }
    a[j+1]=key;

}


}

int main(){
int arr[]={5,4,3,2,1};

int size=sizeof(arr)/sizeof(arr[0]);
    insertionsort(arr,size);
    for(int i=0;i<size;i++){
        printf(" %d",arr[i]);
    }
    printf("\n");
    system("pause");
    return 0;
}