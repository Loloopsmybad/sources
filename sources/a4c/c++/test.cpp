#include <iostream>
#include <string>
using namespace std;
string arra ;
int ara[3]={1,2,34};
string lst[10];
 
int main(){
    getline(cin,arra);
    cout<<"hi "<<arra<<" "<< arra.length()<<endl;
    
    for (int i=0;i<=arra.length();i++){
        cout<<arra[arra.length()-i]<<endl;
    }
for (int i : ara){
    cout<< i;
}
cout<<endl;
int i=0;
while (i<5){
    string a;
    cin>>a;
    lst[i]=a;
    i++;
}
for (string a: lst){
cout<<a<<":::";}
cout<<endl;
system("pause");
return 0;
	
}