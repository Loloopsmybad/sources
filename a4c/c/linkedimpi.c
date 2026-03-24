#include <stdio.h>
#include <stdlib.h>

// Linked list node
typedef struct Node {
    float data;
    struct Node* next;
} Node;

// Create a new node
Node* newNode(float val) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = val;
    node->next = NULL;
    return node;
}

// Insertion sort on a linked list (keeps bucket sorted)
Node* sortedInsert(Node* head, float val) {
    Node* node = newNode(val);

    // Insert at beginning if list is empty or val is smallest
    if (!head || val < head->data) {
        node->next = head;
        return node;
    }

    // Find the correct position
    Node* curr = head;
    while (curr->next && curr->next->data < val)
        curr = curr->next;

    node->next = curr->next;
    curr->next = node;
    return head;
}

// Free all nodes in a linked list
void freeList(Node* head) {
    while (head) {
        Node* tmp = head;
        head = head->next;
        free(tmp);
    }
}

// Bucket Sort (for floats in [0, 1))
void bucketSort(float arr[], int n) {
    // Create n empty buckets (linked lists)
    Node** buckets = (Node**)calloc(n, sizeof(Node*));

    // Distribute elements into buckets
    for (int i = 0; i < n; i++) {
        int idx = (int)(arr[i] * n);   // bucket index
        buckets[idx] = sortedInsert(buckets[idx], arr[i]);
    }

    // Concatenate all buckets back into arr
    int k = 0;
    for (int i = 0; i < n; i++) {
        Node* curr = buckets[i];
        while (curr) {
            arr[k++] = curr->data;
            curr = curr->next;
        }
        freeList(buckets[i]);
    }

    free(buckets);
}

// Print array
void printArr(float arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%.2f ", arr[i]);
    printf("\n");
}

int main() {
    float arr[] = {0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Before: ");
    printArr(arr, n);

    bucketSort(arr, n);

    printf("After:  ");
    printArr(arr, n);

    return 0;
}
```

**Output:**
```
Before: 0.78 0.17 0.39 0.26 0.72 0.94 0.21 0.12 0.23 0.68
After:  0.12 0.17 0.21 0.23 0.26 0.39 0.68 0.72 0.78 0.94