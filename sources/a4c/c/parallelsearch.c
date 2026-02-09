#include<stdio.h>
#include<stdlib.h>

void parallelsearch(int *a1,int *a2,int x){
    int s1=sizeof(a1)/sizeof(a1[0]);
    int s2=sizeof(a2)/sizeof(a2[0]);
    printf("%d",s1);
    printf("%d",s2);
    for (int i=0;i<s1;i++){
        for (int j=0;j<s2;j++){
            if( a1[i]+a2[j]==x){
                printf("%d + %d = %d",a1[i],a2[j], x);
            }
        }
    }
}

int main(){

    int n1;
    int n2;
    int x;
    printf("number of elements in array 1?");
    scanf("%d",&n1);
    int a1[n1];
    for (int j =0;j<n1;j++){
        printf("number ?");
        scanf("%d",&a1[j]);
    }
    printf("number of elements in array 2?");
    scanf("%d",&n2);
    int a2[n2];
    for (int j =0;j<n2;j++){
        printf("number ?");
        scanf("%d",&a2[j]);
    }
    printf("\n");
    for (int j =0;j<n1;j++){
        printf("%d ", a1[j]);
    }
    printf("\n");  
    for (int j =0;j<n2;j++){
        printf("%d ", a2[j]);
    }
    printf("\n");  
    printf("number u want to find pair for ?");
    scanf("%d",&x);
    printf("\n");  
    parallelsearch(a1,a2,x);
    system("pause");
    return 0;
}