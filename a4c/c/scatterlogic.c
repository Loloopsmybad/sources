#include <stdio.h>
#include <stdlib.h>

void insertSorted(int* bucket, int* size, int val) {
    int i = *size - 1;
    while (i >= 0 && bucket[i] > val) {
        bucket[i + 1] = bucket[i];
        i--;
    }
    bucket[i + 1] = val;
    (*size)++;
}

void bucketSort(int* arr, int n) {
    if (n <= 1) return;

    // Step 1: Find min and max
    int min = arr[0], max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < min) min = arr[i];
        if (arr[i] > max) max = arr[i];
    }

    int range = max - min;
    if (range == 0) return;

    // Step 2: Allocate n buckets, each can hold at most n elements
    int** buckets = (int**)calloc(n, sizeof(int*));
    int* sizes    = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++)
        buckets[i] = (int*)malloc(n * sizeof(int));

    // Step 3: Scatter using same formula: (a[i] - min) * (n-1) / range
    for (int i = 0; i < n; i++) {
        int idx = (int)((long long)(arr[i] - min) * (n - 1) / range);
        insertSorted(buckets[idx], &sizes[idx], arr[i]);
    }

    // Step 4: Gather
    int k = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < sizes[i]; j++)
            arr[k++] = buckets[i][j];
        free(buckets[i]);
    }

    free(buckets);
    free(sizes);
}

int main() {
    int arr[] = {-15, 3, -8, 0, 22, -1, 7, -30, 15, 4};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Before: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);

    bucketSort(arr, n);

    printf("\nAfter:  ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
```

**What changed:**

- Each bucket is now a plain `int[]` instead of a linked list
- `insertSorted()` uses **insertion sort style shifting** to keep the bucket sorted as elements come in — no pointers, no malloc per element
- Everything else (scatter formula, gather) is identical to before

**Output:**
```
Before: -15 3 -8 0 22 -1 7 -30 15 4
After:  -30 -15 -8 -1 0 3 4 7 15 22