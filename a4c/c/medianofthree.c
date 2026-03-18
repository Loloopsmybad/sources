#include<stdio.h>
#include <stdlib.h>

int partition(int a[],int start,int end){
    int mid = start + (end -start)/2;
    int median;
    int median_index;
    if (a[start]<a[mid]&&a[mid]<a[end] || a[start]>a[mid]&&a[mid]>a[end] ){
        median=a[mid];
        median_index=mid;
    }else if (a[start]<a[end]&&a[end]<a[mid] || a[start]>a[end]&&a[end]>a[mid] )
    {
        median=a[end];
        median_index=end;
    }
    else{
        median=a[start];
        median_index=start;
    }
    int temp=a[start];
    a[start]=a[median_index];
    a[median_index]=temp;

    median=a[start];
    int index=start;
    for (int i=start+1;i<=end;i++){
        if (a[i]<median){
            index++;
            temp=a[index];
            a[index]=a[i];
            a[i]=temp;
        }

    }
    temp=a[index];
    a[index]=a[start];
    a[start]=temp;
    return index;


}


void quicksort(int arr[],int start ,int end){
    if (start<end){
        int i = partition(arr,start,end);
        quicksort(arr,start,i-1);
        quicksort(arr,i+1,end);
    }
}
void random_number_tester(int n){
    int *a_rand = malloc(n * sizeof(int));
    srand(42);

    for (int i = 0; i < n; i++) {
        a_rand[i] = rand() % 100000;
    }
    printf("before sorting-->\n");
    for (int i=0;i<n;i++){
        printf("%d , ",a_rand[i]);
    }
    printf("----after sorting----");
    quicksort(a_rand,0,n-1);
    for (int i=0;i<n;i++){
        printf("%d , ",a_rand[i]);
    }
    printf("\n");
}
void sorted_number_tester(int n){
    int *a_rand = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        a_rand[i] = i;
    }
    printf("before sorting-->\n");
    for (int i=0;i<n;i++){
        printf("%d , ",a_rand[i]);
    }
    printf("----after sorting----");
    quicksort(a_rand,0,n-1);
    for (int i=0;i<n;i++){
        printf("%d , ",a_rand[i]);
    }
    printf("\n");
}
int main(){
    // int arr[]={10,9,8,7,6,5,4,3,2,1,9,0};
    // int size=sizeof(arr)/sizeof(arr[0]);
    // quicksort(arr,0,size-1);
    int v1=10;
    int v1_1=10;
    int v2=1000;
    int v2_2=1000;
    random_number_tester(v1);
    sorted_number_tester(v1_1);
    random_number_tester(v2);
    sorted_number_tester(v2_2);
    

    // for (int i=0;i<size;i++){
    //     printf("%d ",arr[i]);
    // }
    system("pause");
    return 0;
}