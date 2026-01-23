#include<stdlib.h>
#include<stdio.h>

void merge(int *arr, int left, int mid1, int mid2, int right){
    int len1 = mid1 - left + 1;      // First third length
    int len2 = mid2 - mid1;          // Second third length  
    int len3 = right - mid2;         // Third third length
    
    // Create temporary arrays
    int *arr1 = (int*)malloc(len1 * sizeof(int));
    int *arr2 = (int*)malloc(len2 * sizeof(int));
    int *arr3 = (int*)malloc(len3 * sizeof(int));
    
    // Copy data to temp arrays
    for(int i = 0; i < len1; i++)
        arr1[i] = arr[left + i];
    for(int i = 0; i < len2; i++)
        arr2[i] = arr[mid1 + 1 + i];
    for(int i = 0; i < len3; i++)
        arr3[i] = arr[mid2 + 1 + i];
    
    // Merge the three arrays back
    int i = 0, j = 0, k = 0;
    int pos = left;
    
    // Merge all three while all have elements
    while(i < len1 && j < len2 && k < len3){
        if(arr1[i] <= arr2[j] && arr1[i] <= arr3[k]){
            arr[pos++] = arr1[i++];
        }
        else if(arr2[j] <= arr1[i] && arr2[j] <= arr3[k]){
            arr[pos++] = arr2[j++];
        }
        else{
            arr[pos++] = arr3[k++];
        }
    }
    
    // Merge remaining from arr1 and arr2
    while(i < len1 && j < len2){
        if(arr1[i] <= arr2[j])
            arr[pos++] = arr1[i++];
        else
            arr[pos++] = arr2[j++];
    }
    
    // Merge remaining from arr2 and arr3
    while(j < len2 && k < len3){
        if(arr2[j] <= arr3[k])
            arr[pos++] = arr2[j++];
        else
            arr[pos++] = arr3[k++];
    }
    
    // Merge remaining from arr1 and arr3
    while(i < len1 && k < len3){
        if(arr1[i] <= arr3[k])
            arr[pos++] = arr1[i++];
        else
            arr[pos++] = arr3[k++];
    }
    
    // Copy any remaining elements
    while(i < len1) arr[pos++] = arr1[i++];
    while(j < len2) arr[pos++] = arr2[j++];
    while(k < len3) arr[pos++] = arr3[k++];
    
    free(arr1);
    free(arr2);
    free(arr3);
}

void mergesort(int *arr, int left, int right){
    if(left >= right) // Base case: 1 or 0 elements
        return;
    
    // Calculate the two midpoints to divide into 3 parts
    int mid1 = left + (right - left) / 3;
    int mid2 = left + 2 * (right - left) / 3;
    
    // Recursively sort three parts
    mergesort(arr, left, mid1);
    mergesort(arr, mid1 + 1, mid2);
    mergesort(arr, mid2 + 1, right);
    
    // Merge the three sorted parts
    merge(arr, left, mid1, mid2, right);
}

int main(){
    int n;
    printf("Length of the array? ");
    scanf("%d", &n);
    
    int *arr = (int*)malloc(n * sizeof(int));
    
    for(int i = 0; i < n; i++){
        printf("Value %d: ", i + 1);
        scanf("%d", &arr[i]);
    }
    
    printf("\nThe input array is:\n");
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    mergesort(arr, 0, n - 1);
    
    printf("\nThe sorted array is:\n");
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    free(arr);
    system("pause");
    return 0;
}