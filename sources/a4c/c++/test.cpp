#include <iostream>
#include <string>

using namespace std;


string arra ;
int ara[3]={1,2,34};
string lst[10];
int i=0;
string a;
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



while (true){
        
    getline(cin,a);

    if (a == "END"){
        lst[i]=a;
        break;
    }
    else {
        lst[i]=a;
        i++;
    }
}
getline(cin,a);
for (int i=0;i<a.length();i++){
    char(a[i]);
    cout<<toupper(a[i]);
}
// int p = sizeof(lst)/sizeof(lst[0]);
for (int i = 0; lst[i] != string("END"); i++) {
    cout << lst[i] << ":::";
}


cout<<endl;
system("pause");
return 0;
	
}