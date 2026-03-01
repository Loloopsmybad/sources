#include<stdio.h>
#include<stdlib.h>
int partition(int *a, int start , int end){
int index;
int temp;
int pivot=a[start];
index=start;
for(int i=start+1;i<=end;i++){
    if (a[i]<=pivot){
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
void quicksort(int *a, int start, int end){
if (end<start){
    return;
}
int q=partition(a,start,end);
quicksort(a,start,q-1);
quicksort(a,q+1,end);
}


int main(){
int a[]={5,4,3,2,1,0};
quicksort(a,0,6);
for (int i =0;i<6;i++){
    printf("%d",a[i]);
}
system("pause");
return 0;
}