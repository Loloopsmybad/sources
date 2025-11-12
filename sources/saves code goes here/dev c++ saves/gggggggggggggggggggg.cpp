#include<iostream>

int main()
{
	char st[200];
	
	
	std::cin.getline(st,200);
	
	
	size_t bf = sizeof(st)/sizeof(st[0]);
	
	
	for(int i = bf - 1; i >= 0; i--)
	{
		std::cout<<st[i];

	}
}
