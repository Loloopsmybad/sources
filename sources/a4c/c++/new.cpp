#include <iostream>
#include <list>
#include <stdio.h>
using namespace std;

int main()
{
   
    list<int> myList;

   
    myList.push_back(10);
    myList.push_back(20);
    myList.push_front(5);

    
    cout << "List elements: ";
    for (int n : myList)
    {
        cout << n << " ";
    }
    cout << endl;
	system("pause");
    return 0;
	
	
}
