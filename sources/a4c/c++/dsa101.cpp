#include<iostream>
#include <list>


using namespace std;

int main(){
    int a = -1;
    int spacing =6;
    std::cout<<"hello world"<<endl;
    for (int i=0; i<8;i++){
        for (int k=0; k<=spacing;k++){
            cout<<" ";
        }
        for (int j=0;j<=i;j++){
        cout<<"@";
    a++;
}
       
        for (int p=0; p<a; p++){
        cout<<"@";}
        cout<<endl;
        spacing--;
        a=-1;
        }

spacing=0;
a=6;
        for (int i=0; i<8;i++){
            for (int k=0; k<=spacing;k++){
            cout<<" ";
            }
            for (int j=6;j>=i;j--){
            cout<<"@";
            a--;
            }
       
            for (int p=4; p>=a; p--){
            cout<<"@";}

            cout<<endl;
            spacing++;
            a=6;
        }
    std::getchar();
}