//method 1 using 1 array

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
        while (a<n){
                if (a<(n-1)){
                        arr[a]=arr[a+1];
                        a++;
                }
                else {
                        arr[n-1]=i;
                        a++;
                }
        }

        printf("\n");
        for(int k=0;k<n;k++){
                printf("%d", arr[k]);
        }

return 0;
}



// method 2 using 2 array


// #include<stdio.h>
// #include<stdlib.h>



// int main(){
//         int n=6;
//         scanf("%d",&n);
//         if (n >=100){

//                 printf("length should be less than 100");
//                 return 0;
//         }
//         int arr[n];
//         for(int i =0;i<n;i++){
//         scanf("%d",&arr[i]);
//         }
//         int a=0;
//         int i =0;
//         int j = 1;
//         int arr2[n];
//         while (a<n){
//         arr2[i]=arr[j];
//         a++;
//         i++;
//         j++;
//         }
//         arr2[n-1]=arr[0];


//         for(int i =0;i<n;i++){
//                 printf("%d ", arr2[i]);
//         }


// return 0;
// }
