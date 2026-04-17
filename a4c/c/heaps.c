#include <stdlib.h>
#include <stdio.h>

void swap(int *a,int *b){
    int temp =*a;
    *a=*b;
    *b=temp;
}

void max_heapify(int arr[],int n ,int i){
    int left=2*i+1;
    int right=2*i+2;
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
void buid_max(int arr[],int n){
    for(int i=n/2-1;i>=0;i--){
        max_heapify(arr,n,i);
    }
}

void sort(int arr[],int n){
    buid_max(arr,n);
    for(int i=n-1;i>=0;i--){
        swap(&arr[i],&arr[0]);
        max_heapify(arr,i,0);
    }
}

void heap_sort(int *arr,int n){
    sort(arr,n);
}

int main(){

    int arr[]={23,3,4,5,1,4,33};
    int size=sizeof(arr)/sizeof(arr[0]);
    heap_sort(arr,size);
    for (int i=0;i<size;i++){
        printf("%d : ",arr[i]);
    }

    return 0;
}

// Heapify upward (needed when replaced value is larger than parent)
// void heapify_up(int arr[], int i) {
//     int parent = (i - 1) / 2;
//     if (i > 0 && arr[i] > arr[parent]) {
//         swap(&arr[i], &arr[parent]);
//         heapify_up(arr, parent);
//     }
// }

// // Delete element at a given VALUE (deletes first occurrence)
// int delete_element(int arr[], int *n, int value) {
//     // Step 1: Find the element
//     int index = -1;
//     for (int i = 0; i < *n; i++) {
//         if (arr[i] == value) {
//             index = i;
//             break;
//         }
//     }

//     if (index == -1) {
//         printf("Element %d not found!\n", value);
//         return 0;
//     }

//     // Step 2: Replace with last element
//     arr[index] = arr[*n - 1];

//     // Step 3: Shrink heap
//     (*n)--;

//     // Step 4: Restore heap property
//     heapify_up(arr, index);       // if new value is bigger than parent
//     max_heapify(arr, *n, index);  // if new value is smaller than children

//     return 1;
// }


// int main() {
//     int arr[] = {23, 3, 4, 5, 1, 4, 33};
//     int size = sizeof(arr) / sizeof(arr[0]);

//     // Build a valid max heap first (don't sort — sorting destroys heap structure)
//     buid_max(arr, size);
z
//     printf("Max Heap: ");
//     for (int i = 0; i < size; i++) printf("%d ", arr[i]);
//     printf("\n");

//     // Delete element with value 5
//     delete_element(arr, &size, 5);

//     printf("After deleting 5: ");
//     for (int i = 0; i < size; i++) printf("%d ", arr[i]);
//     printf("\n");

//     return 0;
// }