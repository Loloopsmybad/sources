#include<stdio.h>
#include<stdlib.h>


void selctionsort(int *arr, int size){

    
int left=0;
int right=size-1;
while(left<right){
    int max=left;
    int min=left;
    
    for(int i=left;i<=right;i++){
            if(arr[i]<arr[min]){
                min=i;
            }
            if(arr[i]>arr[max]){
                max=i;
            }
    }
    int temp =arr[left];
    arr[left]=arr[min];
    arr[min]=temp;

    if (max==left){
        max=min;
    }
    temp=arr[right];
    arr[right]=arr[max];
    arr[max]=temp;

    left++;
    right--;

}
}
int main(){
    printf("no of elements ?");
    int n;
    scanf("%d",&n);
    // int arr[n];
    int *arr =(int*)malloc(n*sizeof(int));
    if (arr ==NULL){
     printf("Memory not allocated\n");
    }
    

    for(int i=0;i<n;i++){
        printf("number ? ");
        scanf("%d",&arr[i]);
    }
    printf("\n");

    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    // int size =sizeof(arr)/sizeof(arr[0]);
    selctionsort(arr,n);

    printf("\n");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }

    free(arr);
system("pause");
return 0;
}