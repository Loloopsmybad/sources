#include<stdio.h>
#include<stdlib.h>

void swap(int *a,int*b){
    int temp=*a;
    *a=*b;
    *b=temp;
}

void max_heapify(int arr[], int n,int i ){
    int left=2*i+1;
    int right=2*1+2;
    int largest=i;
    if (left<n && arr[left]>arr[largest]){
        largest=left;
    }
    if (right<n && arr[right]>arr[largest]){
        largest=right;
    }
    if (largest!=i){
        swap(&arr[i],&arr[largest]);
        max_heapify(arr,n,largest);
    }
}

void build_max_heap(int arr[],int n){
    for (int i=n/2-1;i>=0;i--){
        max_heapify(arr,n,i);
    }
}

void heap_sort(int arr[],int n){
    build_max_heap(arr,n);
    for (int i=n-1;i>0;i--){
        swap(&arr[0],&arr[i]);
        n--;
        max_heapify(arr,n,0);
    }
}


int main(){
    int size=0;
    printf("number of elements?");
    scanf("%d",&size);
    int arr[size];
    for (int i=0;i<size;i++){
        printf("number?");
        scanf("%d",&arr[i]);
        printf("\n");
    }
    heap_sort(arr,size);



    for (int i=0;i<size;i++){
        printf("%d ",arr[i]);
    }

    system("pause");
    return 0;
}