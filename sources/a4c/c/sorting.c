#include<stdio.h>
#include<stdlib.h>
int key=0;
int arr[10];
int size = 10;

void insort(int arr[10],int size){
    // int size = sizeof(arr)/sizeof(arr[0]); 
    int j=0;
    for (int i=1 ; i<size;i++){
        key = arr[i];
        j=i-1;
        while(j>=0 && arr[j]>key){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=key;
    }
    printf("\n");
    for(int k = 0; k<10;k++){
        printf("%d ",arr[k]);
    }
    

}

int main(){
    
    for(int p=0; p<10;p++){
        scanf("%d", &arr[p]);
    }
    printf("\n");
    for(int k = 0; k<10;k++){
        printf("%d,",arr[k]);
    }
    insort(arr,size);
    system("pause");
    return 0;

}