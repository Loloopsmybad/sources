
#include<stdio.h>
#include<stdlib.h>

void selectionsort(int *arr, int *size){
    int i=0,j=0;
    int temp=arr[0];
    int temp_val;
    int temp_index;
    printf("______%d______",(*size));
    while (i<=(*size)-1){
        
        if (arr[j]<=temp){
            temp=arr[j];
            temp_index=j;
            j++;
        }else{
            j++;
        }
        if (j==(*size)){
            temp_val=arr[i];
            arr[i]=temp;
            arr[temp_index]=temp_val;
            i++;
            j=i;    
            temp=arr[i];
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
