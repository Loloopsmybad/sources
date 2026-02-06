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
int main(){
    int n;
    printf("number of elements?");
    scanf("%d",&n);
    int a[n];
    for (int j =0;j<n;j++){
        printf("number ?");
        scanf("%d",&a[j]);
    }
    printf("\n");
    for (int j =0;j<n;j++){
        printf("%d ", a[j]);
    }
    quicksort(a,0,(n-1));
    printf("\n sorted \n");
    for (int y =0;y<n;y++){
        printf("%d ", a[y]);
    }
    system("pause");
    return 0;
}