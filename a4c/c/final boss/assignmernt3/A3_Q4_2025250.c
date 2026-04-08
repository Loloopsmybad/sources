#include<stdio.h>
#include<stdlib.h>



typedef struct tree{
    struct tree* p;
    struct tree* root;
    struct tree* right;
    int key;
    struct tree* left;
} tree;



void insert_tree(tree* bst, tree* z){
    tree * y =NULL;
    tree * x =bst->root;
    while(x!=NULL){
        y=x;
        if (z->key<x->key){
            x=x->left;
        }else{
            x=x->right;
        }
    }
    z->p=y;
    if (y==NULL){
        bst->root=z;
    }else if(z->key<y->key){
        y->left=z;
    }else{
        y->right=z;
    }
}

void insert(tree* bst ,int v){
    tree* n=(tree*)malloc(sizeof(tree));
    n->key=v;
    n->left = NULL;    
    n->right = NULL;   
    n->p = NULL;           
    n->root = NULL;  
    insert_tree(bst,n); 
}



void walk(tree * bst){
    tree* x =bst->root;
    while (x!=NULL)
    {
        if (x->left==NULL){
            printf("%d : ",x->key);
            x=x->right;
        }
        else
        {
            tree *pre=x->left;
            while(pre->right!=NULL && pre->right!=x){
                pre=pre->right;
            }
            if(pre->right==NULL){
                pre->right=x;
                x=x->left;
            }
            else{
                pre->right=NULL;
                printf("%d : ",x->key);
                x=x->right;
            }
        }
    }

}



tree* search(tree* bst,int k){
    if (bst==NULL|| k==bst->key){
        return bst;
    }
    if (k<bst->key){
        return search(bst->left,k);
    }else{
        return search(bst->right,k);
    }
}

void predecessor(tree*x){
    if(x->left!=NULL){
        x=x->left;
        while(x->right!= NULL){
            x=x->right;
        }
        printf("successor is : %d \n",x->key);
        return;
    }
    tree * y= x->p;
    
    while ( y!=NULL && x==y->left){
        x=y;
        y=y->p;
    }
    if (y!=NULL){
            printf("successor is : %d \n",y->key);
        }
    else{
        printf("NULL \n");
    }
    }
void find_and_search(tree* bst,int num){
    tree*num_ptr=search(bst,num);
    predecessor(num_ptr);
}

int main(){
    tree* bst=(tree *)malloc(sizeof(tree));
    bst->root  = NULL;
    bst->left  = NULL;
    bst->right = NULL;
    bst->p     = NULL;
    
    insert(bst,15);
    insert(bst,6);
    insert(bst,18);
    insert(bst,3);
    insert(bst,7);
    insert(bst,17);
    insert(bst,20);
    insert(bst,2);
    insert(bst,4);
    insert(bst,13);
    walk(bst);
    printf("\n");
    find_and_search(bst->root,20);
    find_and_search(bst->root,17);
    find_and_search(bst->root,13);
    find_and_search(bst->root,2);
    
    system("pause");
    return 0;
}
