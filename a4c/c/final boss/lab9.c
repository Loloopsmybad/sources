#include<stdlib.h>
#include<stdio.h>

typedef struct tree{
    int key;
    struct tree *root;
    struct tree *p;
    struct tree *left;
    struct tree *right;
}tree;



void insert_tree(tree*bst , tree*z){
    tree* y=NULL;
    tree *x=bst->root;
    while(x!=NULL){
        y=x;
        if(z->key<x->key){
            x=x->left;
        }
        else{
            x=x->right;
        }
    }
    z->p=y;
    if(y==NULL){
        bst->root=z;
    }
    else if(z->key<y->key){
        y->left=z;
    }else{
        y->right=z;
    }
}
void insert(tree*bst,int v){
    tree* n=(tree*)malloc(sizeof(tree));
    n->key=v;
    n->left=NULL;
    n->right=NULL;
    n->p=NULL;
    n->root=NULL;
    insert_tree(bst,n);
}


void walk(tree* bst){
    if (bst!=NULL){
        walk(bst->left);
        printf("%d : ",bst->key);
        walk(bst->right);
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
    printf("found : %d ",bst->key);
}

void transplant(tree*bst,tree *u, tree *v){
    if(u->p==NULL){
        bst->root=v;
    }
    else if(u==u->p->left){
        u->p->left=v;
    }else{
        u->p->right=v;
    }
    if (v!=NULL){
        v->p=u->p;
    }
}
tree* minimum(tree* bst){
    while(bst->left!=NULL){
        bst=bst->left;
    }
    return bst;

}

void delete(tree* bst, tree * z){
    if (z->left==NULL){
        transplant(bst,z,z->right);
    }
    else if(z->right=NULL){
        transplant(bst,z,z->left);
    }
    else{
        tree * y=minimum(z->right);
        if (y->p!=z){
            transplant(bst,y,y->right);
            y->right=z->right;
            y->right->p=y;
        }
        transplant(bst,z,y);
        y->left=z->left;
        y->left->p=y;
    }

}
void find_and_delete(tree*bst,int x){
    tree* temp=search(bst,x);
    delete(bst,temp);
}

int main(){
    tree * bst=(tree*)malloc(sizeof(malloc));

    bst->left=NULL;
    bst->right=NULL;
    bst->p=NULL;
    bst->root=NULL;


    printf("testcase1");
    insert(bst,50);
    insert(bst,30);
    insert(bst,70);
    insert(bst,60);
    insert(bst,80);
    walk(bst->root);
    printf("\n");
    find_and_delete(bst->root,30);
    walk(bst->root);

    

    system("pause");
    return 0;
}
