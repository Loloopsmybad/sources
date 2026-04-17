#include <stdio.h>
#include <string.h>
#include <stdlib.h>
    
#define SIZE 10
int table[SIZE];

// Hash function: key % SIZE
int hash(int key) {
    return key % SIZE;
}

// Insert using linear probing
void insert(int key) {
    int index = hash(key);

    // Probe until we find an empty or deleted slot
    for (int i = 0; i < SIZE; i++) {
        int newIndex = (index + i) % SIZE;  // +1 each time, wrap around

        if (table[newIndex] == -1) {
            table[newIndex] = key;
            printf("Inserted %d at index %d\n", key, newIndex);
            return;
        }
    }
    printf("Hash table is full! Could not insert %d\n", key);
}

// Search using linear probing
int search(int key) {
    int index = hash(key);

    for (int i = 0; i < SIZE; i++) {
        int newIndex = (index + i) % SIZE;

        if (table[newIndex] == -1) {
            return -1;  // Empty slot means key doesn't exist
        }
        if (table[newIndex] == key) {
            return newIndex;  // Found it!
        }
        // If -2 (deleted), keep probing
    }
    return -1;  // Not found
}

// Delete using linear probing
void delete(int key) {
    int index = search(key);
    if (index == -1) {
        printf("Key %d not found!\n", key);
    } else {
        table[index] = -1;  // Mark as deleted (not just empty)
        printf("Deleted %d from index %d\n", key, index);
    }
}

// Print the table
void display() {
    printf("\nHash Table:\n");
    for (int i = 0; i < SIZE; i++) {
        if (table[i] == -1)
            printf("  [%d] : empty\n", i);
        else
            printf("  [%d] : %d\n", i, table[i]);
    }
    printf("\n");
}

int main() {
    // Initialize table as empty (-1)
    for (int i = 0; i < SIZE; i++)
        table[i] = -1;

    insert(10);  // hash = 0
    insert(20);  // hash = 0  → collision → goes to 1
    insert(35);  // hash = 5
    insert(45);  // hash = 5  → collision → goes to 6
    insert(15);  // hash = 5  → collision → goes to 7

    display();

    printf("Search 45: found at index %d\n", search(45));
    printf("Search 99: found at index %d\n\n", search(99));

    delete(20);
    display();
    system("pause");
    return 0;
}