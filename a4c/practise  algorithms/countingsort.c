#include<stdio.h>
#include<stdlib.h>


void countingsort(int arr[],int size){
    int x= arr[0];
    for (int i =0;i<size;i++){
        if (arr[i]>x){
            x = arr[i];
        }
    }
    int min = arr[0];
    for (int i = 0; i < size; i++) {
        if (arr[i] < min) min = arr[i];
    }
    x++;
    
    int range = x - min + 1;
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
    int arr[]={10,9,8,7,6,5,4,3,2,1,-1,-4,-3};
    int size = sizeof(arr)/sizeof(arr[0]);
    countingsort(arr,size);
    system("pause");
    return 0;

}
