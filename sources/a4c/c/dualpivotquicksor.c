#include <stdio.h>
#include <stdlib.h>
// void divide(int a[], int low, int high, int *p, int *q)
// {
//     if (a[low] > a[high]) {
//         int t = a[low];
//         a[low] = a[high];
//         a[high] = t;
//     }

//     int pivot1 = a[low];
//     int pivot2 = a[high];

//     int i = low + 1;
//     int lt = low + 1;
//     int gt = high - 1;

//     while (i <= gt) {
//         if (a[i] < pivot1) {
//             int t = a[i];
//             a[i] = a[lt];
//             a[lt] = t;
//             lt++;
//         }
//         else if (a[i] > pivot2) {
//             int t = a[i];
//             a[i] = a[gt];
//             a[gt] = t;
//             gt--;
//             i--;   // re-check swapped element
//         }
//         i++;
//     }

//     lt--;
//     gt++;

//     int t = a[low];
//     a[low] = a[lt];
//     a[lt] = t;

//     t = a[high];
//     a[high] = a[gt];
//     a[gt] = t;

//     *p = lt;
//     *q = gt;
// }

void divide(int *a,int s,int e,int *fst, int *snd){
    int x = a[e];
    int index=e;
    int b_index=s;
    int temp;
    
    for (int i =(e-1);i>=s;i--){
        if(a[i]>=x){
            index--;
            temp=a[index];
            a[index]=a[i];
            a[i]=temp;
        }  else if (a[i]<=x){
            b_index++;
            temp=a[b_index];
            a[b_index]=a[i];
            a[i]=temp;
            i--;
        }
    }
    temp=a[e];
    a[e]=a[index];
    a[index]=temp;

    temp=a[s];
    a[s]=a[b_index];
    a[b_index]=temp;

    *fst=index;
    *snd=b_index;
}

void quicksort(int *a,int start,int end, int *fst,int *snd){
if (start<=end){
divide(a,start,end,fst,snd);
int q=*fst;
int p=*snd;
quicksort(a,start,q-1,fst,snd);//left
quicksort(a,q+1,p-1,fst,snd);//right
quicksort(a,p+1,end,fst,snd);
}
}
int main(){
    int n;
    printf("number of elements?");
    scanf("%d",&n);
    int a[n];
    int fst;
    int snd;
    for (int j =0;j<n;j++){
        printf("number ?");
        scanf("%d",&a[j]);
    }
    printf("\n");
    for (int j =0;j<n;j++){
        printf("%d ", a[j]);
    }
    quicksort(a,0,(n-1),&fst,&snd);
    printf("\n sorted \n");
    for (int y =0;y<n;y++){
        printf("%d ", a[y]);
    }
    system("pause");
    return 0;
}