#include<iostream>
using namespace std;

int b;
int choice;
int c=0;
class node{
public:
    int value;
    node* Next;
};
//0-head,1-old,2-replace
node*ptrarr[3];

void linkedlist(node* address){
    while (address!=NULL){
        cout<<address<<":"<< &address<<":"<<address->Next<<":"<<address->value<<endl;
        address=address->Next;
    }
}
void add_ele(){
    node* a=new node();
    cout<<"what will be the value? of new node: ";
    cin>>b;
    cout<<endl;
    a->value=b;
    if (c==0){
        ptrarr[0]=a;
        // node**p=&a;
        c++;
    }
    else{
        c=2;
    }
    ptrarr[1]=a;
}
int main(){
    while (true)
    {
        add_ele();
        if (c>=2){
            ptrarr[2]->Next=ptrarr[1];
        }
        cout<<"do you want to add more element 1for yes 2 for no: ";
        cin>>choice;
        cout<<endl;
        if (choice==1){
            ptrarr[2]=ptrarr[1];
        }
        else{
                ptrarr[1]->Next=NULL;
                // *p->Next=NULL;
                linkedlist(ptrarr[0]);
                // linkedlist(p);
                break;
        }
    }
    system("pause");
}
//pointer of a class is essentailly creating new objects of that class 
//class_name *ptr_name[4] so we just created 4 new objects of that class where each object is following the basic structure
// #include <iostream>
// using namespace std;

// class Node {
// public:
//     int Value;
//     Node* Next;
// };
// void printList(Node* n) {
//     while (n!=NULL) {
//         cout << n->Value << endl;
//         n = n->Next;
//     }
// }

// int main()
// {
//     Node* head = new Node();
//     Node* second = new Node();
//     Node* third = new Node();

//     head->Value = 1;
//     head->Next = second;
//     second->Value = 2;
//     second->Next = third;
//     third->Value = 3;
//     third->Next = NULL;
    
//     printList(head);

//     system("pause>0");
// }