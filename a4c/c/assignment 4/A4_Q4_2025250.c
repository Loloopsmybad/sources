#include <stdio.h>
#include<stdlib.h>

void swap(int*a,int*b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void maxHeapify(int arr[],int n,int i) { 
    int left = 2*i+1;
    int right = 2*i+2;
    int largest =i;

    if(left<n && arr[left]>arr[largest]){
        largest =left;
    }
    if(right<n && arr[right]>arr[largest]){
        largest =right;
    }
    if(largest != i){
        swap(&arr[i], &arr[largest]);
        maxHeapify(arr,n,largest); 
    }
}

void buildMaxHeap(int arr[],int n) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        maxHeapify(arr, n, i);
    }
}

void print_A(int arr[],int n){
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    // int n;
    // scanf("%d", &n);

    int n1=6;
    int n1_a[]={10,3,5,7,2,8};

    int n2=5;
    int n2_a[]={4,1,3,16,45};

    // int arr[n];
    // for (int i = 0; i < n; i++)
    //     scanf("%d", &arr[i]);


    buildMaxHeap(n1_a, n1);
    buildMaxHeap(n2_a, n2);
    // buildMaxHeap(arr, n);
    print_A(n1_a,n1);
    print_A(n2_a,n2);
    // print_A(arr,n);

    system("pause");
    return 0;
}