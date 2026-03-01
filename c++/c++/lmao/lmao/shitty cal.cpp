
#include <iostream>


int a;
int b;
char op;
int c;
using namespace std;


int main()
{

 for(;;)
	{

	cin >> a;
	cin >> b;
	cin >> op;
		switch (op)
		{
		case '+':
			c = a + b;
			cout << c ;
			break;
		case '-':
			c = a - b;
			cout << c;
			break;
		case '*':
			c = a * b;
			cout << c;
			break;
		case '/':
			c = a / b;
			cout << c;
			break;
		}
	}

}











// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
