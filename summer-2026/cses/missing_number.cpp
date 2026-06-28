#include<iostream>
#include<cstdlib>
using namespace std;

void co_sort(int *arr,int n){
    int x=arr[0];
    for (int i =0 ;i<n-1;i++){
        if (arr[i]>x){
            x=arr[i];
        }
    }
    int temp[x];

    for (int i =0;i<x;i++){
        temp[i]=0;
    }
    for (int i =0 ;i<n-1;i++){
        temp[arr[i]]++;
    }
int p=0;
    for(int i=1;i<x;i++){
        if (temp[i]==0){
            cout<<i;
            p++;
            break;

        }
    }
    if (p==0){
        cout<<x+1;
    }
    
        
}


int main(){
    int n=0;
    cin>>n;
    int arr[n-1];
    for (int i =0;i<n-1;i++){
        cin>>arr[i];
    }
    co_sort(arr,n);


    system("pause");
    return 0;
}
