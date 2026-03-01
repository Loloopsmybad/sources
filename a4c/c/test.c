#include<stdio.h>
#include<stdlib.h>


int main(){
        int n;
        scanf("%d",&n);
        if (n >=100){

                printf("length should be less than 100");
                return 0;
        }
        int arr[n];
        for(int i =0;i<n;i++){
        scanf("%d",&arr[i]);
        }
        int a=0;
        int i = arr[0];
        printf("%d",i);
        while (a<=5){
                arr[a]=arr[a+1];
                a++;
        }

        arr[5]=i;
        for(int i =0;i<n;i++){
                printf("%d ", arr[i]);
        }

system("pause");
return 0;
}