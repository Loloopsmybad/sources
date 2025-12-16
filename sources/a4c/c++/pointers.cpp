#include <iostream>
using namespace std;

int myfunc(int *x) {
    cout<<*x;
  return *x=5 + *x;
}

int main() {
  int a=4;
  cout << myfunc(&a);
  cout<<a;
  system("pause");
  return 0;
}