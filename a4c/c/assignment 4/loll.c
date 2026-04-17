#include<stdio.h>
#include<stdlib.h>

int m;               
int *array;
int collisions;

int hash(int key){
    return (key % m);
}

int insert(int key){
    int index = hash(key);

    for(int i = 0; i < m; i++){
        int newindex = (index + i*i) % m;

        if(array[newindex] == -1){
            //printf("index %d is empty so we add %d\n", newindex, key);
            array[newindex] = key;
            return newindex;
        }
        else{
            collisions++;
            printf("collision index %d occupied by %d\n", newindex, array[newindex]);
        }
    }
    printf("table is full could not insert %d \n", key);
    return -1;
}

int search(int key){
    int index = hash(key);

    for(int i = 0; i < m; i++){
        int newindex = (index + i*i) % m;  

        if(array[newindex] == key){
            printf("FOUND %d at index %d\n", key, newindex);
            return newindex;       
        }
        if(array[newindex] == -1){
            printf("NOT FOUND %d\n", key);
            return -1;
        }
    }
    printf("NOT FOUND %d\n", key);
    return -1;
}

void delete(int key) {
    int index = search(key);
    if (index == -1) {
        //printf("Key %d not found!\n", key);
        return;
    } else {
        array[index] = -1;
        printf("Deleted %d from index %d\n", key, index);
    }
}

void display(){
    for(int i = 0; i < m; i++){    
        if(array[i] == -1){
            printf("at index %d array is empty\n", i);
        }
        else{
            printf("%d: %d\n", i, array[i]);
        }
    }
}

int main(){
    // scanf("%d",&m);
    // array[m];
    m=4;
    array = malloc(m * sizeof(int));
    for(int i = 0; i < m; i++){   
        array[i] = -1;
    }

    // for(int i = 0; i < m; i++){   
    //     sacnf("%d",&array[i]);
    // }

    insert(10);
    insert(15);
    insert(20);
    search(15);
    delete(67);
    search(15);

    // insert(10);
    // insert(17);
    // insert(24);
    // insert(17);
    // search(24);
    // delete(17);
    // search(17);

    printf("=============================display hash table==========================\n");
    display();

    printf("collisions are %d\n", collisions);
    system("pause");
    return 0;
}