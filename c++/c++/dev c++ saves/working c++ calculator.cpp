#include<iostream> 

double a=0,b=0;
using namespace std ;
char op;
int main()
{

	for(;;)
	{
		cin >> a;
		cin >> op;
			if(op =='+')
			{
				b+=a;
				cout << b << '\n' ;
			}
			if(op =='-')
			{
				b-=a;
				cout << b << '\n' ;
			}
			if(op =='*')
			{
				b*=a;
				cout << b << '\n' ;
			}
			if(op =='/')
			{
				b/=a;
				cout << b << '\n' ;
			}
	}

	
	
}
