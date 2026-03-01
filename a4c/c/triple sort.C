#include<stdlib.h>
#include<stdio.h>

void merge(int *arr , int f, int s,int t , int left, int right){
int f_l=f-left;//first arry length
int s_l=(t-1)-(f+1);//second arry length
int t_l=right-t;//third arry length


//creating array for the respective first second and third array as well as a temp array for string the sorted elements from first and second array
int f_arr[f_l];
int s_arr[s_l];
int temp[f_l+s_l];
int t_arr[t_l];

int move = left;

for (int i =0;i<f_l;i++){
f_arr[i]=arr[f+i];
}
for(int i =0;i<s_l;i++){
s_arr[i]=arr[s+i];
}
for(int i =0;i<t_l;i++){
t_arr[i]=arr[t+i];
}
// this part is for sorting left and right array
int i,j,k,l=0;
for(int k =left;k<=t-1;k++){
    if (f_arr[i]<=s_arr[j]){
        temp[k]=f_arr[i];
        i++;
    }else{
        temp[k]=s_arr[j];
        j++;
    }
    move++;
}
// this part for moving left over elements from first arry adn second arry to main arry
while(i<f_l){
arr[move]=f_arr[i];
i++;
move++;
}
while (j<s_l){
    arr[move]=s_arr[j];
    j++;
    move++;
}
for(int p =0; p<t-1;p++){
    printf("%d ", arr[i]);

}

int t1=0;
int t_2=0;
// this part is for sorting left and right array
for(int l=t;l<=right;k++){
    if (t_arr[t1]<=temp[t1]){
        arr[l]=temp[t1];
        t1++;
    }else{
        arr[l]=t_arr[t_2];
        t_2++;
    }
    move++;
}
// this part for moving left over elements from temp arry to main arry
while(i<(f_l+s_l)){arr[move]=temp[i];i++;}
while(j<t_l){arr[move]=s_arr[i];j++;}

}

void mergesort(int *arr, int left , int right){
// int total=left+right+1;//total length of array
//int total = right - left  // corrected
// if ((right-left+1)<=3){//base case if the length of the array is less than equal to 3 return
//     return;
// }

if(left >= right) // this is the correct base case since the 
        return;//abbove base case will stop when the asub array length is 3 and there will be no sorting since the merge function will also not be called ass return comes before it     
//no need for these !!!

//int d3=total/3;
// int f=1;
// int s=1;
// int t=1;
// int s_end=0;

// f=d3-1;//end of first array
// s=f+1;//starting of second array
// t=(d3*2);//starting of third array
// s_end=t-1;//end of second array

// Calculate the two midpoints to divide into 3 parts
int mid1 = left + (right - left) / 3;
int mid2 = left + 2 * (right - left) / 3;
    
// mergesort(arr ,left,f);
mergesort(arr ,left,mid1);
// mergesort(arr,s,s_end);
mergesort(arr ,mid1,mid2);
// mergesort(arr,t,right);
mergesort(arr ,mid2+1,right);
merge(arr,mid1,mid2,left,right);
}
int main(){
    int n;
    printf("length of the array ?");
    scanf("%d",&n);
    int arr[n];
    for (int b =0;b<n;b++){//adding elements in the array
        printf("\n value ?");
        scanf("%d",&arr[b]);
    }
    printf("\n");
    printf("\nthe input array is \n");
    for (int b =0;b<n;b++){
        printf("value -> %d", arr[b]);// printing the array
    }
    int length = sizeof(arr)/sizeof(arr[0]);
    mergesort(arr, 0 ,length);
    system("pause");
    return 0;
}

