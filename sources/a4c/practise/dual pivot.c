#include<stdio.h>
#include<stdlib.h>
int p1, p2;
void partition(int *a,int s, int e){
int temp;
int index=s;
int index2=e-1;
int key=a[s];
int key2=a[e];
for(int i=s+1;i<=e;i++){
    if(a[i]<=key){
        index++;
        temp =a[index];
        a[index]=a[i];
        a[i]=temp;
    }else if(a[i]>=key2){
        index2--;
        temp =a[index2];
        a[index2]=a[i];
        a[i]=temp;
    }
}
temp=a[index];
a[index]=a[s];
a[s]=temp;

temp=a[index2];
a[index2]=a[e];
a[e]=temp;

p1=index;
p2=index2;
}
void quicksort(int *a, int start, int end) {
    if (end <= start) return;  // changed < to <=
    
    partition(a, start, end);
    int lp = p1, rp = p2;
    
    quicksort(a, start, lp - 1);
    quicksort(a, lp + 1, rp - 1);
    quicksort(a, rp + 1, end);
}
//not working
int main() {
    int a[] = {5, 4, 3, 2, 1, 0};
    quicksort(a, 0, 5);  // 5 not 6
   
    for (int i =0;i<6;i++){
    printf("%d",a[i]);
    }

    system("pause");
    return 0;
}