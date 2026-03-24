#include <stdio.h>
#include <stdlib.h>

void insertionSort(int *bucket, int size) {
    for (int i = 1; i < size; i++) {
        int key = bucket[i];
        int j = i - 1;
        while (j >= 0 && bucket[j] > key) {
            bucket[j+1] = bucket[j];
            j--;
        }
        bucket[j+1] = key;
    }
}

void bucketSort(int *arr, int n) {

    int max = arr[0];
    int min = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
    }

    int bucketSize = (max - min) / n + 1;

    int buckets[n][n];
    int bucketCount[n];
    for (int i = 0; i < n; i++) bucketCount[i] = 0;

    for (int i = 0; i < n; i++) {
        int index = (arr[i] - min) / bucketSize;
        buckets[index][bucketCount[index]] = arr[i];
        bucketCount[index]++;
    }


    int pos = 0;
    for (int i = 0; i < n; i++) {
        insertionSort(buckets[i], bucketCount[i]);
        for (int j = 0; j < bucketCount[i]; j++)
            arr[pos++] = buckets[i][j];
    }
}

int main() {
    int arr[] = {42, 10, 78, 25, 63, 5, 90, 33, 55, 18};
    int n = 10;
    bucketSort(arr, n);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    system("pause");
    return 0;
}