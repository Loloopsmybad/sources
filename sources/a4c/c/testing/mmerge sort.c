#include<stdlib.h>
#include <stdio.h>

void mergesort(int *arr,int left ,int right){
if (left <= right) {
return;
}
int (*mid) = (right - left)/2;
mergesort( arr, left , mid);
mergesort(arr,mid +1 , right);

merge(&arr,&right, &left, &mid);

}

void merge(int *arr, int *left , int *right , int *mid ){

int size1= (*mid) - (*left);
int size2= (*right)+ ((*mid)+1);

int s1[size1];
int s2[size2];

for (int i=0;i<size1;i++){
s1[i]=arr[ (*left) +i];
}
for (int i=0;i<size2;i++){
s1[i]=arr[ (*mid)+1 +i];
}
int i,j;
i=0;
j=0;

while (i<size1 && j<size2){
    if (s1[i]<s2[j]){
        
    }

}

}
int main(){



}
