#include<stdio.h>
#include<stdlib.h>

void selectio_sort(int * a,int x){
    int i=0;
    int j=1;
    int temp;
    while(i<x){
        if (a[j]<=a[i]){
            temp=a[j];
            a[j]=a[i];
            a[i]=temp;
            j++;
        }
        else{
            j++;
        }
        if(j==x){
            i++;
            j=i;
        }

    }


}


int main(){
    int a[]={9,8,7,6,5,4,3,2,1};
    int size=sizeof(a)/sizeof(a[0]);
    selectio_sort(a,size);
    for (int i=0;i<size;i++){
        printf("%d",a[i]);
    }
    system("pause");
    return 0;
}