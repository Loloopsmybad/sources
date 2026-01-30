#include<stdio.h>
#include<stdlib.h>

void selectionsort(int *arr, int *size){
    int i=0,j=0;
    int temp;
    printf("______%d______",(*size));
    while (i<=(*size)-1){
        // printf("no i: %d j: %d size: %d",i,j,(*size));
        if (arr[j]<arr[i]){
            
            temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
            j++;
        }else{
            j++;
        }
        if (j==(*size)){
            // printf("hi");
            i++;
            j=i;    
        }
    }
}



int main(){
    printf("no of elements ?");
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        printf("number ? ");
        scanf("%d",&arr[i]);
    }
    printf("\n");
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
    int size =sizeof(arr)/sizeof(arr[0]);

    selectionsort(arr,&size);
    for(int i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
system("pause");
return 0;

}