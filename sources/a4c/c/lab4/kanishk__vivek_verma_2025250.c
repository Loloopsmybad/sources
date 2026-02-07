#include <stdio.h>
#include <stdlib.h>
#include <time.h>
// int randomPivot ( int low , int high ) {
// srand((unsigned int)time(NULL));
// int d =low + rand () % ( high - low + 1) ;
// return d;
//  }
int divide(int *a,int s,int e){
    srand((int)time(NULL));
    int d =rand () % ((e-s)+1) ;
    printf("\n random number generated is : %d \n",d);

    int tempo;
    tempo=a[s];
    a[s]=a[d];
    a[d]=tempo;

    int x = a[s];
    int index=s;
    int temp;
    
    for (int i=s+1;i<=e;i++){
        if(a[i]<=x){
            index++;
            temp=a[index];
            a[index]=a[i];
            a[i]=temp;
        }
    }
    temp=a[s];
    a[s]=a[index];
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

    for (int y =0;y<n;y++){
        printf("%d ", a[y]);
    }
    system("pause");
    return 0;
}