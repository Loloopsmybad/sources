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


void linkedlist(node* address){
    while ((address)!=NULL){
        cout<<(address)<<":"<<(address)->Next<<":"<<(address)->value<<endl;
        (address)=(address)->Next;
    }
}
node *header;
node *previous;
node *current;
void add_ele_back(){
    while (true)
    {
        
        node* a=new node();
        cout<<"what will be the value? of new node: ";
        cin>>b;
        cout<<endl;
        a->value=b;
        if (c>0){
            cout<<(previous)->value<<endl;
            (previous)->Next=a;
            
        }
        
        if (c==0){
            header=a;
            c++;
        }
        previous=a;
        current=a;
        cout<<"do you want to add an element 1 for yes else 2 for no: ";
        cin>>choice;
        cout<<endl;
        if (choice==2){
            (current)->Next=NULL;
            linkedlist(header);
            break; 
            }
    }
}
void add_ele_front(){
    while (true)
    {
        node* a=new node();
        cout<<"what will be the value? of new node: ";
        cin>>b;
        cout<<endl;
        a->value=b;
        if (c>0){
            a->Next=header;
        }
        else{
            c++;
            a->Next=NULL;
        }
        header=a;
        cout<<"do you want to add an element 1 for yes else 2 for no: ";
        cin>>choice;
        cout<<endl;
        if (choice==2){
            linkedlist(header);
            break; 
            }


    }


}
int main(){
    // add_ele_back();
    add_ele_front();
    system("pause");
}
