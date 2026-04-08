#include<stdlib.h>
#include<stdio.h>

typedef struct tree{
    int key;
    int height;
    struct tree *root;
    struct tree *p;
    struct tree *left;
    struct tree *right;
}tree;


int height(tree* n) {
    if (n == NULL){
        return 0;
    }
    else{
        return n->height;
    }
    
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

void update_height(tree* n) {
    if (n != NULL)
        n->height = 1 + max(height(n->left), height(n->right));
}

// Balance factor: left height - right height
// AVL rule: this must stay between -1 and +1
int get_balance(tree* n) {
    return (n == NULL) ? 0 : height(n->left) - height(n->right);
}

tree* rotate_right(tree* bst_wrapper, tree* y) {
    tree* x = y->left;
    tree* B = x->right;

    // Perform rotation
    x->right = y;
    y->left = B;

    // Fix parent pointers
    x->p = y->p;
    y->p = x;
    if (B != NULL) {
        B->p = y;
    }

    // Fix parent's child pointer
    if (x->p == NULL)
        bst_wrapper->root = x;
    else if (x->p->left == y)
        x->p->left = x;
    else
        x->p->right = x;

    // Update heights (y first since it's now lower)
    update_height(y);
    update_height(x);

    return x;
}

tree* rotate_left(tree* bst_wrapper, tree* x) {
    tree* y = x->right;
    tree* B = y->left;

    // Perform rotation
    y->left = x;
    x->right = B;

    // Fix parent pointers
    y->p = x->p;
    x->p = y;
    if (B != NULL){
         B->p = x;
    }
    
    // Fix parent's child pointer
    if (y->p == NULL)
        bst_wrapper->root = y;
    else if (y->p->left == x)
        y->p->left = y;
    else
        y->p->right = y;

    // Update heights
    update_height(x);
    update_height(y);

    return y;
}
void rebalance(tree* bst, tree* n) {
    while (n != NULL) {
        update_height(n);
        int bal = get_balance(n);

        // Left heavy
        if (bal > 1) {
            if (get_balance(n->left) < 0)
                rotate_left(bst, n->left);   // Left-Right case
            rotate_right(bst, n);
        }
        // Right heavy
        else if (bal < -1) {
            if (get_balance(n->right) > 0)
                rotate_right(bst, n->right); // Right-Left case
            rotate_left(bst, n);
        }

        n = n->p; // walk up to root
    }
}

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
    rebalance(bst, n);
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


void delete(tree* bst, tree * z, tree** rebalance_start){
    if (z->left==NULL){
        transplant(bst,z,z->right);
    }
    else if(z->right==NULL){
        transplant(bst,z,z->left);
    }
    else{
        tree * y=minimum(z->right);
        *rebalance_start = y->p;
        if (y->p!=z){
            transplant(bst,y,y->right);
            y->right=z->right;
            y->right->p=y;
        }else{
            *rebalance_start = y;
        }
         transplant(bst,z,y);
        y->left=z->left;
        y->left->p=y;
    }
}


void find_and_delete(tree*bst,int x){
    tree* temp=search(bst->root,x);

    //talk about this 
    if (temp != NULL) {
        tree* parent = temp->p; 
        tree* rebalance_start = NULL;
        delete(bst, temp,&rebalance_start);
        rebalance(bst,rebalance_start);
    } else {
        printf("Key %d not found\n", x);
    }
}


int main(){
    tree * bst=(tree*)malloc(sizeof(tree));
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
    find_and_delete(bst,30);
    walk(bst->root);

    

    system("pause");
    return 0;
}
