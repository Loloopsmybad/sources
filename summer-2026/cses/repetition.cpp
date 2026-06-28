#include<iostream>
#include<cstdlib>
#include <string>
using namespace std;

int main(){
    char x;
    cin>>x;
    int size=sizeof(x)/sizeof("A");
    char strin[size]=x;



    system("pause");;
    return 0;
}