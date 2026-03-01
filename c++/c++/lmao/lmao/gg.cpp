#include <iostream>
using namespace std;
int const size = 500;
char op[size] = {0};

int main()
{
	cin.getline(op, size);
	for (int i = 0; i < size; i++)
		cout << op[i];


}
