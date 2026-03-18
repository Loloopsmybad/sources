#include <stdio.h>
#include <stdlib.h>

int divide(int *a,int s,int e){
    int x = a[e];
    int index=e;
    int temp;
    for (int i =(e-1);i>=s;i--){
        if(a[i]>=x){
            index--;
            temp=a[index];
            a[index]=a[i];
            a[i]=temp;
        }
    }
    temp=a[e];
    a[e]=a[index];
    a[index]=temp;
    return index;
}

void quicksort(int *a,int start,int end){
if (start<=end){
int q=divide(a,start,end);
quicksort(a,start,q-1);//left
quicksort(a,q+1,end);//right
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