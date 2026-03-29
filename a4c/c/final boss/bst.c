#include<stdio.h>
#include<stdlib.h>



typedef struct tree{
    struct tree* p;
    struct tree* root;
    struct tree* right_node;
    int key;
    struct tree* left_node;
} tree;



void insert_tree(tree* bst, tree* z){
    tree * y =NULL;
    tree * x =bst->root;
    while(x!=NULL){
        y=x;
        if (z->key<x->key){
            x=x->left_node;
        }else{
            x=x->right_node;
        }
    }
    z->p=y;
    if (y==NULL){
        bst->root=z;
    }else if(z->key<y->key){
        y->left_node=z;
    }else{
        y->right_node=z;
    }
}

void insert(tree* bst ,int v){
    tree* n=(tree*)malloc(sizeof(tree));
    n->key=v;
    n->left_node = NULL;    
    n->right_node = NULL;   
    n->p = NULL;           
    n->root = NULL;  
    insert_tree(bst,n); 
}

tree* minimum(tree * x){
    while(x->left_node!= NULL){
        x=x->left_node;
    }
    printf("%d",x->key);
    return x;
}

tree* maximum(tree*x){
    while(x->right_node!= NULL){
        x=x->right_node;
    }
    printf("%d",x->key);
    return x;

}

tree* search(tree *x,int k){
    if (x == NULL || k==x->key){
        return x;
    }
    if (k<x->key){
        return search(x->left_node,k);
    }else{
        return search(x->right_node,k);
    }
}

void delete(){



}

void transplant(){



}

tree* successor(tree*x){
    if(x->right_node!=NULL){
        return minimum(x->right_node);
    }
    tree * y= x->p;
    while ( y!=NULL && x==y->right_node){
        x=y;
        y=y->p;
    }
    printf("%d",y);
    return y;
}
void walk(tree * bst){
    if (bst!=NULL){
        walk(bst->left_node);
        printf("%d : ",bst->key);
        walk(bst->right_node);
    }
}




int main(){
    tree* bst=(tree *)malloc(sizeof(tree));
    bst->root = NULL;
    bst->left_node=NULL;
    bst->right_node=NULL;
    bst->p=NULL;
    
    insert(bst,10);
    insert(bst,5);
    insert(bst,1);
    insert(bst,4);
    insert(bst,34);
    walk(bst->root);
    printf("\n");
    minimum(bst->root);
    printf("\n");
    maximum(bst->root);
    printf("\n");
    successor(bst->root);
    printf("\n");
    
    system("pause");
    return 0;
}
