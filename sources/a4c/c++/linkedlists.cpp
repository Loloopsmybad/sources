#include<iostream>
using namespace std;
string a;
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
        cout<<address<<":";
        cout<<address->Next<<":";
        cout<<address->value<<endl;
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
        if (choice==1){
            ptrarr[2]=ptrarr[1];
        }
        else{
                ptrarr[1]->Next=NULL;
                linkedlist(ptrarr[0]);
                break;
        }
    }
    // node* head =new node();
    // node* second =new node();
    // node* third=new node();
    
    // head->value=1;
    // second->value=2;
    // third->value=3;
    // head->Next=second;
    // second->Next=third;
    // third->Next=NULL;

    // add_ele();
    // linkedlist(head);

    system("pause");
}