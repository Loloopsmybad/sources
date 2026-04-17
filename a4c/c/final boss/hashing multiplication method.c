#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int array[16];
int o =-1;

int hash(int key) {
    int long long A = 2654435769;
    int long long val = key * A % 4294967296;  //4294967296 is 2^w 
    int long long x = val >> (32-4);         
    return (int)x;
}

void insert(int key){
    int index=hash(key);

    for (int i=0;i<16;i++){
        int newindex=(index+i*i)%16;
        if (array[newindex]==-1){
            printf("index %d is empty so we add %d\n",i,key);
            array[newindex]=key;
            return;
        }
        else if (array[newindex]!= o){
            printf("%d collision ! index occupied by %d\n",i,array[i]);
        }
        
    }
    printf("value not found!");
}

int search(int key){
    int index=hash(key);

    for (int i=0;i<16;i++){
        int newindex=(index+i*i)%16;
        if (array[newindex]==-1){
            return -1;
        }
        else if (array[newindex]==-1){
            return (array[newindex]);
        }
    }
    return -1;
}

void display(){
    for(int i =0;i<16;i++){
        if (array[i]==-1){
            printf("at index %d array is empty\n",i);
        }
        else{
            printf("at index %d the element is %d \n",i,array[i]);
        }
    }
}
int main(){
    for(int i=0;i<16;i++){
        array[i]=-1;
    }
    insert(65);
    insert(50);
    insert(25);
    insert(79);
    insert(67);
    insert(24);
    insert(89);
    insert(44);
    insert(75);
    insert(38);
    printf("=============================display hash table==========================");
    display();
    printf("there are more number of collisions in division method and less in multiplication\n");
    printf("last answer--> multiplication method because multilpication method is less affected by array size");
    system("pause");
    return 0;
}
