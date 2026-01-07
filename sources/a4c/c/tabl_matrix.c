#include <stdio.h>
#include <stdlib.h>

int main(){
    int a ;
    scanf("%d",&a);
    for(int i=1 ; i < 10 ; i++){
        for (int j =0; j<=a;j++){
        printf("%d ",j*i);
    }
        printf("\n");
    }
    // return 0;
    system("pause");
}
