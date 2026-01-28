#include<stdio.h>
#include<stdlib.h>
void reverse(int *arr,int n){
    int key=0;
    for (int i =0;i<(n/2);i++){
    key=arr[n-i-1];
    arr[n-i-1]=arr[i];
    arr[i]=key;
}
for(int i =0;i<n;i++){
    printf("%d",arr[i]);
}
}

int main(){
    int n;
    printf("length -> ?");
    scanf("%d",&n);
    int arr[n];
    for(int i =0;i<n;i++){
        printf("VALUE : ?");
        scanf("%d",&arr[i]);
    }
    printf("\n");
    reverse(arr,n);
    system("pause");
    return 0;
}