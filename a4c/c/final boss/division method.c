#include<stdio.h>
#include<stdlib.h>

int array[11];
int collisions;

int hash(int key){
    return (key % 11);
}


int insert(int key){
    int index=hash(key);

    for (int i=0;i<11;i++){
        int newindex=(index+i*i)%11;
        
       if (array[newindex]==-1){
            printf("index %d is empty so we add %d\n",i,key);
            array[newindex]=key;
            return -1;
        }
        else{
            collisions++;
            printf("%d collision index occupied by %d\n",i,array[i]);
        }
        
    }
    return -1;
}

int search(int key){
    int index=hash(key);

    for (int i=0;i<11;i++){
        int newindex=(index+i*i)%11;
        if (array[newindex]==-1){
            return -1;
        }
    }
    return -1;
}

void display(){
    for(int i =0;i<11;i++){
        if (array[i]==-1){
            printf("at index %d array is empty\n",i);
        }
        else{
            printf("at index %d the element is %d \n",i,array[i]);
        }
    }
}
int main(){
    for(int i=0;i<11;i++){
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


    printf("collisions are %d",collisions);
    printf("there are more number of collisions in division method and less in multiplication\n");
    printf("last answer--> multiplication method because multilpication method is less affected by array size");
    system("pause");
    return 0;
}



































