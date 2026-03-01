#include<stdio.h>
#include<stdlib.h>

int p=1;

int main(){
    p=1;
    for(int i=7;i>=0;i--){
        for(int k=i;k>0;k--){
            printf(" ");
            
        }
        for(int j = 0;j<p;j++){
              printf("*");
        }
        for(int t = 1;t<p;t++){
              printf("*");
        }
        p++;
        printf("\n");
    }p=1;
        
    for(int i=7;i>=0;i--){
        for(int k=0;k<p;k++){
            printf(" ");
            
        }
        for(int j = i;j>0;j--){
              printf("*");
        }
        for(int t = i;t>1;t--){
              printf("*");
        }
        p++;

        printf("\n");
        
    }  
    


    

    system("pause");
    return 0;
}