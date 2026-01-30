#include<stdlib.h>
#include <stdio.h>

void merge(int *arr, int *left , int *right , int *mid ){

    int size1= (*mid) - (*left)+1;
    int size2= (*right)- (*mid);

    int s1[size1];
    int s2[size2];

    for (int i=0;i<size1;i++){
        s1[i]=arr[(*left) +i];
    }

    for (int i=0;i<size2;i++){
        s2[i]=arr[(*mid)+1 +i];
    }

    int i=0,j=0,t=(*left);

    while ( i<size1 && j < size2 ){
        if (s1[i]<=s2[j])
        { 
            arr[t]=s1[i];
            i++;
        }else{arr[t]=s2[j];
              j++;
            }
        t++;
        }
        while(i<size1){
            arr[t]=s1[i];
            i++;
            t++;
        }
        while(j<size2){
            arr[t]=s2[j];
            j++;
            t++;
        }

}

void mergesort(int *arr,int left ,int right){
    if (left >= right) {
        return;
    }

    int mid = left+((right - left)/2);
    mergesort( arr, left , mid);
    mergesort(arr,mid+1, right);
    merge(arr,&left,&right,&mid);

}


int main(){
    int n;
    printf("number ?");
    scanf("%d",&n);
    int arr[n];
    for(int i =0 ; i<n;i++){
        printf("number ? ");
        scanf("%d",&arr[i]);
    }
    for (int i=0;i<n;i++){
        printf("%d",arr[i]);
    }
    int left;
    int right;
    right= (sizeof(arr)/sizeof(arr[0]))-1;
    left=0;
    mergesort(arr,left,right);
    printf("\n");
    for (int i=0;i<n;i++){
        printf("%d",arr[i]);
    }
 system("pause");
 return 0;

}
