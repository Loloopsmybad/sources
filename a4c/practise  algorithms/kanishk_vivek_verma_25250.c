#include<stdlib.h>
#include<stdio.h>

void countingsort(int *arr,int size){
    int x=arr[0];
    
    for (int i=0 ;i<size;i++){
        if (arr[i]>x){
            x=arr[i];
        }
    }
    int min=arr[0];
    for (int i=0 ;i<size;i++){
        if (arr[i]<min){
            min=arr[i];
        }
    }
     x++;
    // int index[x];
    int range = x - min + 1;  // x is your max
    int index[range];
    int output[size];

    for (int i =0;i<range;i++){
        index[i]=0;
    }
    for (int i =0;i<size;i++){
        // index[arr[i]]++;
        index[arr[i] - min]++;
    }
    for(int i =1; i<range;i++){
        index[i]=index[i-1]+index[i];
    }

    for (int i=size-1;i>=0;i--){
        output[index[arr[i] - min] - 1] = arr[i];
        index[arr[i] - min]--;
    }
    for (int i=0;i<size;i++){
        printf("%d ",output[i]);
    }
}

int main(){

    int n;
    printf("size?");
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
    int size = sizeof(arr)/sizeof(arr[0]);
    countingsort(arr,size);

    system("pause");
    return 0;
}
