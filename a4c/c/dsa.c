#include <stdio.h>
#include <stdlib.h>
int num;
int main() {
  scanf("%d",&num);

  for(int i=2 ; i<=num; i++){
    for (int j=1;j<=10;j++){
          printf("%d - ",i*j);
    }
    printf("\n");
  }
  system("pause");
  return 0;
}