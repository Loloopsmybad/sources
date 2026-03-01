#include<iostream>

using namespace std;

void num_ele(int LOL[] , int boo)
{
	for(int i ; i < boo; i++)
	{
		cout << LOL << '\t' ;
	}
	
}
int main()
{
	const int size = 100;
	
	
	int LOL[size];

    int boo = 0;


for(int i ; i < size ; i++)
{	


	if(cin >> LOL[i])
	{
		boo++;
	}
	else
	{
		break;
	}
	
	
	
}

	num_ele(LOL,boo);
	
}



//	int size = sizeof(LOL)/sizeof(LOL[0]) ;
