#include <stdio.h>
#include <stdlib.h>



int binarysearch(int*a2,int n,int req){
    int left = 0;
    int right = n - 1;
    while(left <= right) {
    int mid = left + (right - left) / 2;
    if (a2[mid] == req){
        return mid;
        }
    else if (a2[mid] < req){
        left = mid + 1;
        }
    else{
        right = mid - 1;
        }
    }
    return -1;
}


void search(int *a1, int * a2, int n, int x) {
    for (int i = 0; i < n; i++) {
        int required = x - a1[i];
        int right_ptr = binarysearch(a2, n, required);
        if (right_ptr != -1){
            printf(" pair is { %d + %d } = %d \n", a1[i],a2[right_ptr],x);
            return;
        }
    }
}

int main() {
    int n;
    int x;
    
    printf("enter the size of arrays: ");
    scanf("%d", &n);
    
    int a1[n]; 
    int a2[n];
    
    printf("enter %d elements of array A: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a1[i]);
    }
    
    printf("enter %d elements of array B: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a2[i]);
    }
    
    printf("the target sum x: ");
    scanf("%d", &x);
    
    search(a1,a2,n,x);
    system("pause");
    return 0;
}