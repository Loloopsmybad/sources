#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Node for linked list (each bucket)
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Insert into bucket (sorted insertion)
void insertSorted(Node** bucket, int val) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = NULL;

    if (*bucket == NULL || (*bucket)->data >= val) {
        newNode->next = *bucket;
        *bucket = newNode;
        return;
    }

    Node* curr = *bucket;
    while (curr->next && curr->next->data < val)
        curr = curr->next;
    newNode->next = curr->next;
    curr->next = newNode;
}

void bucketSort(int* arr, int n) {
    if (n <= 1) return;

    // Find min and max
    int min = arr[0], max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < min) min = arr[i];
        if (arr[i] > max) max = arr[i];
    }

    int range = max - min + 1;
    int bucketCount = n; // Use n buckets

    Node** buckets = (Node**)calloc(bucketCount, sizeof(Node*));

    // Distribute elements into buckets
    for (int i = 0; i < n; i++) {
        // Normalize: shift so min maps to 0
        int idx = (int)(((long long)(arr[i] - min) * (bucketCount - 1)) / range);
        insertSorted(&buckets[idx], arr[i]);
    }

    // Collect elements back
    int k = 0;
    for (int i = 0; i < bucketCount; i++) {
        Node* curr = buckets[i];
        while (curr) {
            arr[k++] = curr->data;
            Node* tmp = curr;
            curr = curr->next;
            free(tmp);
        }
    }

    free(buckets);
}

int main() {
    int arr[] = {-15, 3, -8, 0, 22, -1, 7, -30, 15, 4};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Before: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    bucketSort(arr, n);

    printf("After:  ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
```

**Key idea — handling negatives:**

The trick is **normalization**. Instead of using raw values as bucket indices (which breaks for negatives), shift everything so the minimum maps to 0:
```
idx = ((arr[i] - min) * (bucketCount - 1)) / range
```

This maps any value — positive or negative — into the range `[0, bucketCount-1]`.

**How it works step by step:**

1. **Find min/max** → compute the range of values
2. **Normalize** each element to get its bucket index (no negative indices possible)
3. **Sorted insertion** into each bucket (linked list keeps bucket sorted as elements arrive)
4. **Concatenate** all buckets back into the array

**Output:**
```
Before: -15 3 -8 0 22 -1 7 -30 15 4
After:  -30 -15 -8 -1 0 3 4 7 15 22