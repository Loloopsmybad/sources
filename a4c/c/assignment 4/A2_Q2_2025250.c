#include <stdio.h>
#include <stdlib.h>


#define MAX_CHAIN 10  

int m;
int array[100][MAX_CHAIN]; 
int chainsize[100];        

int hash(int key) {
    return (key % m);
}

void insert(int key) {
    int index = hash(key);

    for (int i = 0; i < chainsize[index]; i++) {
        if (array[index][i] == key){
            return;
        }
    }
    if (chainsize[index] < MAX_CHAIN) {
        array[index][chainsize[index]] = key;
        chainsize[index]++;
    }
    else{
        printf("chain at %d is full \n", index);
    }
}

void search(int key) {
    int index = hash(key);

    for (int i=0; i < chainsize[index]; i++) {
        if (array[index][i] == key) {
            printf("FOUND\n");
            return;
        }
    }
    printf("NOT FOUND\n");
}

void delete(int key) {
    int index = hash(key);

    for (int i=0; i < chainsize[index]; i++) {
        if (array[index][i] == key) {
            for (int j = i; j < chainsize[index] - 1; j++) {
                array[index][j] = array[index][j + 1];
            }
            chainsize[index]--;
            return;
        }
    }
}

void display() {
    printf("Final Table:\n");
    for (int i = 0; i < m; i++) {
        printf("%d:",i);

        for (int j = 0; j < chainsize[i]; j++) {
            printf(" %d", array[i][j]);
            if (j < chainsize[i] - 1){
                  printf(" ->");
            }
        }
        printf("\n");
    }
}
void test_case_1(){
    m=5;

    for (int i = 0; i < m; i++){
        chainsize[i] = 0;
    }
    insert(10);
    insert(15);
    insert(20);
    search(15);
    delete(15);
    search(15);
    display();

}
void test_case_2(){
    m=7;

    for (int i = 0; i < m; i++){
        chainsize[i] = 0;
    }
    insert(10);
    insert(17);
    insert(24);
    insert(31);
    search(24);
    delete(17);
    search(17);
    display();

}
int main() {

    //==============please uncomment this part if you want to take input 
     
    // int n;
    // scanf("%d %d", &m, &n);

    // for (int i = 0; i < m; i++)
    //     chainSize[i] = 0;

    // char op[10];
    // int key;
    // for (int i = 0; i < n; i++) {
    //     printf(" opertaion I -> INSERT , S -> SEARCH , D -> DELETE");
    //     printf("\n");
    //     scanf("%s", op);
    //     printf("\n");
    //     printf("key ?");
    //     scanf("%d",&key);
    //     if(op[0] == 'I') {
    //         insert(key);
    //     }
    //     else if(op[0] == 'S'){ 
    //         search(key);
    //     }
    //     else if(op[0] == 'D'){ 
    //         delete(key);
    //     }
    // }

    test_case_1();
    printf("===================test case 2======================");
    test_case_2();
    system("pause");
    return 0;
}