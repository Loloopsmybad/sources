#include<stdlib.h>
#include<stdio.h>
float *a1;
void insertionsort(float arr[], int size) {
    for (int i = 1; i < size; i++) {
        float key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;   
    }
}

void bucketsort(float *arr, int n) {

    float buckets[n][n];
    int bucketcount[n];

    for (int i = 0; i < n; i++) {
        bucketcount[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        int index = n*arr[i];
        buckets[index][bucketcount[index]++] = arr[i];
    }
    for(int i = 0 ;i <n;i++){
        insertionsort(buckets[i], bucketcount[i]);
    }

    int pos = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < bucketcount[i]; j++)
            arr[pos++] = buckets[i][j];
    }

    for (int i=0;i<5;i++){
            printf("%.2f : ",arr[i]);
    }
}


int main(){
    // float arr[]={0.78,0.17,0.39,0.26,0.72};
    int n;
    printf("size?");
    scanf("%d ",&n);

    float arr[n];

    

    for (int i=0 ;i<n;i++ ){
        printf("enternumber");
        scanf("%f",&arr[i]);
    }
    bucketsort(arr,5);



    system("pause");
    return 0;
}
