#include<iostream>
using namespace std;
string a;
int b;
int choice;
class node{
public:
    int value;
    node* Next;
};
node*ptrarr[1];

void linkedlist(node* address){
    while (address!=NULL){
        cout<<address<<":";
        cout<<address->Next<<":";
        cout<<address->value<<endl;
        address=address->Next;
    }
}

void add_ele(){
    cout<<"node number?: ";
    cin>>a;
    cout<<endl;
    node* a=new node();
    cout<<"waht will be the value?: ";
    cin>>b;
    cout<<endl;
    a->value=b;
    a->Next=NULL;
    linkedlist(a);
}


int main(){

    // node* head =new node();
    // node* second =new node();
    // node* third=new node();
    
    // head->value=1;
    // second->value=2;
    // third->value=3;
    // head->Next=second;
    // second->Next=third;
    // third->Next=NULL;
    while (true)
    {
        cout<<"node number?: ";
        cin>>a;
        cout<<endl;
        node* a=new node();
        cout<<"what will be the value?: ";
        cin>>b;
        cout<<endl;
        a->value=b;
        a->Next=NULL;
        cout<<"do you want to add more element 1for yes 2 for no: ";
        cin>>choice;
        if (choice==1){
            continue;
        }
        else{
                ptrarr[0]=a;
                linkedlist(ptrarr[0]);
                break;
        }
    }
    
    
    
    // add_ele();
    // linkedlist(head);

    system("pause");
}