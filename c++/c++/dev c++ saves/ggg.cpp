#include<iostream>


void print_array(char f,int size)
{
	for(int i=0 ; i<size ;i++)
	{
		//std::cout<<f[i]<<'\n';
		if(f==' ')
		{
			std::cout<<f<<'\n';
		}
		else
		{
		std::cout<<f;	
		}
	}
}

int main()
{
	char st[200];
	std::cin.getline(st,200);
	
	print_array(st,200);
}
