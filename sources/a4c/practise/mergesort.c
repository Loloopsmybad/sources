#include<stdio.h>
#include<stdlib.h>

void merge(int *a,int start,int mid,int end){
int left=mid-start+1;
int right=end-mid;
int lefta[left];
int righta[right];
for (int i=0;i<left;i++){
lefta[i]=a[start+i];
}
for (int i=0;i<right;i++){
righta[i]=a[mid+i+1];
}

int i =0;
int j =0;
int k=start;
while (i<left && j<right){
       if(lefta[i]<=righta[j]){
        a[k]=lefta[i];
        i++;
        } 
       else{
        a[k]=righta[j];
        j++;
        }
        k++;
}
while(i<left){
    a[k]=lefta[i];
    i++;
    k++;
}
while(j<right)
{
    a[k]=righta[j];
    j++;
    k++;
}

}

void merge_sort(int *a,int start,int end){
if(end<=start){
    return ;
}
int mid = (start+end)/2;
merge_sort(a,start,mid);
merge_sort(a,mid+1,end);
merge(a,start,mid,end);
}



int main(){

    int arr[]={5,4,3,2,1};
    merge_sort(arr,0,5);    
for(int i =0; i<5;i++){
    printf("%d",arr[i]);
}
    system("pause");
    return 0;
}