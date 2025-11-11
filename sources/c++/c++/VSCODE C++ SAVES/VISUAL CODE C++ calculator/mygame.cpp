#include  <iostream>
#include  <string> 
#include <conio.h>   

#define KEY_UP 87//w
#define KEY_DOWN 83//s
#define KEY_LEFT 65//a
#define KEY_RIGHT 68//d
using namespace std ;
char op; 
int A;
void key_up()
{
     for (int i = 0; i <= 5; i++)
    {
     cout<<i;
    }
    
  
}
void key_right()
{
     for (int i = 0; i <= 5; i++)
    {
     cout<<i;
    }
    
  
}void key_down()
{
     for (int i = 0; i <= 5; i++)
    {
     cout<<i;
    }
    
  
}
void key_left()
{
     for (int i = 0; i <= 5; i++)
    {
     cout<<i;
    }
    
  
}
int main()
{
  
   switch (getch())
   {
     case KEY_UP:
      for (int i = 0; i <= 5; i++)
      {
       cout<<i;
      }
      key_up();
      break;

     case KEY_DOWN:
      key_down();
      break;
     
     case KEY_LEFT:
      key_left();
      break;
     
     case KEY_RIGHT:
      key_right();
      break;
      
   }
  
}
