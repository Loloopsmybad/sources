#include<iostream>
#include<cstdlib>
using namespace std;

int main(){
    unsigned long n=0;
    cin>>n;
    cout<<n<<" ";
    while(n!=1){
        if(n%2==0){
            n=n/2;
            cout<<n<<" ";
        }
        else{
            n=n*3;
            n=n+1;
            cout<<n<<" ";
        }
    }


    system("pause");
    return 0;    
}

