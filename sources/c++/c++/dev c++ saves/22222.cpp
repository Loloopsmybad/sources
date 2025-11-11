#include <iostream> 
#include<conio.h>
using namespace std;

int main()
{
   
    int SIZE_OF_ARRAY = 500;
	
	char MY_ARRAY[SIZE_OF_ARRAY]={0};

	 while((MY_ARRAY[SIZE_OF_ARRAY]=getch())!='\r')
    {	
	SIZE_OF_ARRAY++;
	cin.getline(MY_ARRAY,SIZE_OF_ARRAY);
   
    }

	
	//size_t size_of_ARRAY = sizeof(MY_ARRAY)/sizeof(MY_ARRAY[0]);
	//if you don't want to output the arry in opposit direction "ulta direction " use:-
	// for(int i = 0 ; i < SIZE_OF_ARRAY; i++)
		
    for(int i = SIZE_OF_ARRAY ; i >= 0; i--)
	{
		cout<< MY_ARRAY[i] ;
	}
 

}
