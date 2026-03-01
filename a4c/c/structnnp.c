#include<stdio.h>
#include<stdlib.h>

typedef struct{
    int id;
    float temp;
}sensor;

int main(){
    int n=0;
    printf("number of sensors ???? ");
    scanf("%d",&n);
    sensor *s1=(sensor*)malloc(n*sizeof(sensor));
    for(int j=1;j<=n;j++){
        printf("\nEnter data for sensor : %d\n ",j);
        printf("Sensor ID:");
        scanf("%d",&s1->id);
        printf("Temperature:");
        scanf("%f",&s1->temp);
        s1++;
    }
    s1--;
    printf("\n");
    for(int i=n;i>0;i--){
        printf("sensor ID : %d \n",s1->id);
        printf("Temperature: %f \n",s1->temp);
        s1--;
    }
    
    system("pause");
    return 0;
}


