#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include<string.h>
bool isValid(char* s) {
        int a= strlen(s);
        int i=0;
        while(i<=((a/2)-1)){
            
            if (s[i]=='(' && s[(a-1)-i]==')'){
                i++;
                printf("hi1");
            }
            else if (s[i]=='{' && s[(a-1)-i]=='}'){
                i++;
                printf("hi2");
            }
            else if (s[i]=='[' && s[(a-1)-i]==']'){
                i++;
                printf("hi2");
            }
            else {
                // printf("hi");
                return false;
                break;
            }
            // i++;
        }
            return true;
}
int main(){
    char a[]="()";
    isValid(&a);

    system ("pause");
    return 0;
}