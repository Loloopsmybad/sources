#include<iostream>


void print_array(char f[],int size)
{
	for(int i=0 ; i<size ;i++)
	{
		//std::cout<<f[i]<<'\n';
		if(f[i]==' ')
		{
			std::cout<<f[i]<<'\n';
		}
		else
		{
		std::cout<<f[i];	
		}
	}
}

int main()
{
	char st[200];
	std::cin.getline(st,200);
	
	print_array(st,200);
}
