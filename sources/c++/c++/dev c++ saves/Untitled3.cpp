#include<iostream>
#include<string>


using namespace std;

string nig(string str, char c)
{
     
    for(int i=0;i<str.length();i++) 
    {
        if(str[i]!=1)
		{
		  
        cout << str[i];
        	 cout<<str[i];
        }
        else 
		{
    	str[i] + '\n'; 
    	     cout<<str[i];
    	 }
    }

}

int main()
{
string aa;
//char OP[5000]; 
cin >> aa;
char c = ' ';
aa=nig(aa,c);

}
