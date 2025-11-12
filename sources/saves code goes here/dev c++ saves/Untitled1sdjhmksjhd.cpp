#include<iostream>
void print_array(char f[],int size)
{
	for(int i=0 ; i<size ;i++)
	{
		std::cout<<f[i]<<'\n';
	}
}

int main()
{
	char st[200];
	std::cin.getline(st,200);
		//int size =sizeof(st)/sizeof(st);
		print_array(st,200);
}
