#include<stdlib.h>
#include<stdio.h>

int main(){
    int x=0;
    scanf("%d",&x);
    int lis[x];
    int index=0;
    for (int i=0;i<x;i++){
        int a=0;
        int b=0;
        scanf("%d %d", &a, &b);
        int xy[a];
        for (int i = 0; i < a; i++)
        {
            scanf(" %d",&xy[i]);
        }
        if (b<2){
            int check=xy[0];
            for(int i=1;i<a;i++){
                if (check>xy[i]){
                    printf("NO\n");
                    // lis[index]=0;
                    // index++;
                    check=99;
                    break;
                }else{
                check=xy[i];
                }
            }
            if (check!=99){
                printf("YES\n");
                // lis[index]=1;
                //     index++;
            }
            
           
            
        }
        else{
            printf("YES\n");
            // lis[index]=1;
            // index++;
        }
    }
    // for (int i = 0; i < x; i++)
    // {
    //     if(lis[i]==0){
    //         printf("NO\n");
    //     }else{
    //         printf("YES\n");
    //     }
    // }
    
   
}