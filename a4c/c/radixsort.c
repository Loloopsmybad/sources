#include<stdlib.h>
#include<stdio.h>
#include<string.h>

void stablesort(int *a,int pos,int size){
    int count[10]={0};
    int divisor = 1;
    for (int i = 0; i < pos - 1; i++){
        divisor *= 10;
    }
    // then count digits of ALL elements
    for (int i = 0; i < size; i++) {
        count[(a[i] / divisor) % 10]++;
    }
    for(int i=1;i<10;i++){
        count[i]=count[i-1]+count[i];
    }
    int output[size];
    for (int i = size-1;i>=0;i--){
        int digit = (a[i] / divisor) % 10;
        output[count[digit]-1]=a[i];
        count[digit]--;
    }
    memcpy(a, output, size * sizeof(int)); 
}

void radix_sort(int *arr,int size){
    int min = arr[0];
    for (int i = 1; i < size; i++)
        if (arr[i] < min) min = arr[i];
    
    if (min < 0) {
        for (int i = 0; i < size; i++)
            arr[i] -= min;  // shift all to >= 0
    }

    int x =arr[0];
    for (int i =0;i<size;i++){
        if (arr[i]>x){
            x=arr[i];
        }
    }
    int digits=0;
    while(x!=0){
        x=x/10;
        digits++;
    }
    for(int i=1;i<=digits;i++){
        stablesort(arr,i,size);
    }
    if (min < 0) {
        for (int i = 0; i < size; i++)
            arr[i] += min;
    }
    for(int i=0;i<size;i++){
        printf("%d : ",arr[i]);
    }

}






int main(){

    int arr[]={-10,19,-23,2,3,1,24,40,-3};
    int size=sizeof(arr)/sizeof(arr[0]);
    radix_sort(arr,size);
    system("pause");
    return 0;
}