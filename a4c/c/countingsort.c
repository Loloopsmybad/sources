#include <stdio.h>
#include <stdlib.h>

int counting_sort(int *arr,int n){

    int x=arr[0];
    for (int i=0;i<n;i++){
        if (x<arr[i]){
            x=arr[i];
        }
    }
    int *index=(int *)malloc(x*sizeof(int));
    int *output=(int *)malloc(n*sizeof(int));
    
    for(int i=0;i<=x;i++){
        index[i]=0;
    }
    for (int i=0;i<n;i++){
        index[arr[i]]++;
    }
    for(int i=1;i<=x;i++){
        index[i]=index[i]+index[i-1];
    }
    for (int i=x-1;i>=0;i--){
        output[index[arr[i]]-1]=arr[i];
        index[arr[i]]--;
    }

    return output;
}
int main(){
    int arr[]={11,10,9,8,7,6,5,4,3,2,1};
    int size=sizeof(arr)/sizeof(arr[0]);
    int *sorted_arr=counting_sort(arr,size);
    for (int i = 0; i < size; i++) {
        printf("%d ", sorted_arr[i]);
    }

    system("pause");
    return 0;
}