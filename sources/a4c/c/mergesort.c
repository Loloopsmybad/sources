#include <stdio.h>
#include <stdlib.h>


void mergesort(int *arr,int left ,int right){
    if(left>=right){
        return;
    }
    int mid=(left +right)/2;
    mergesort(arr,left ,mid);
    mergesort(arr,mid+1 ,right);
    merge(arr,left,right,mid);
}

void merge(int *arr, int left , int right, int mid ){

int l_arr=mid-left+1;   //+1 cuz length starts from 1 
int r_arr=right-mid;

int lefta[l_arr+1];
int righta[r_arr+1];
int move=left;

for(int i =0;i<l_arr;i++){
lefta[i]=arr[left+i];//-1 cuz 0 based indexing
}

for (int j =0;j<r_arr;j++){
righta[j]=arr[mid+j+1];
}

lefta[l_arr+1]=99999;
righta[r_arr+1]=99999;

int i =0;
int j= 0;

for(int k =left;k<=right;k++){
    if (lefta[i]<=righta[j]){
        arr[k]=lefta[i];
        i++;

    }else{
        arr[k]=righta[j];
        j++;
    }
    move++;
}
while (i<lefta){
                arr[move] = lefta[i];
                move++;
                i++;
            }

        // Copy the remaining elements of left_arr[], if any
while (j<righta)
        {
                arr[move] = righta[j++];
                move++;
                j++;
            }

    }

int main(){
    system("pause");
    return 0;
}