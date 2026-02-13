

typedef struct node {
    int key;
    struct node* next;
    struct node *prev;
}node;
typedef struct list {
    struct node* head;
    struct node* tail;
 }list;
void list_prepend(struct list* L, struct node* x)
{   
    if (L->head==0){
        return;
    }
    
        x->next=L->head;
       (L->head)->prev=x;
       L->head=x;
       (L->head)->prev=NULL;       
}

void list_insert_after(struct node* y, struct node* x)
{
    if (y == 0) {
    return;
    }
        x->prev=y;
        x->next = y->next;
        (y->next)->prev=x;
        y->next = x;       
}

 void list_delete(struct list* L, struct node* prev, struct node* x)
 {
    if (x==0){
        return;
    }
    if (prev==0){
        L->head = x->next;
        (x->next)->prev=L->head;
    }else{
     prev->next=x->next;
     x->next->prev=prev;
    }
    
   
 }

 void example()
 {
        struct list L;
        struct node a, b, c;
        L.head=0;
        a.key = 10;a.next = 0;
        b.key = 20;b.next = 0;
        c.key = 30;c.next = 0;

        /* Prepend with checks (matches pseudocode) */
        list_prepend(&L, &a); /* 10 */
        list_prepend(&L, &b); /* 20 -> 10 */


        /* Insert-after with y == NIL check */
        list_insert_after(&b, &c); /* 20 -> 30 -> 10 */

        /* Delete with x == NIL check; delete c with prev = b */
        list_delete(&L, &b, &c); /* 20 -> 10 */
}


///this is the edited code