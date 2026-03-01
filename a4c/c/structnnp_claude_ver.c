#include<stdio.h>
#include<stdlib.h>

typedef struct{
    int id;
    float temp;
}sensor;

int main(){
    int n=0;
    printf("Enter number of sensors: ");
    scanf("%d", &n);  // Removed \n
    
    // Allocate memory for n sensors
    sensor *s1 = (sensor*)malloc(n * sizeof(sensor));
    
    if(s1 == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    sensor *ptr = s1;  // Save original pointer
    
    for(int j = 0; j < n; j++){
        printf("\nEnter data for sensor %d:\n", j+1);
        printf("Sensor ID: ");
        scanf("%d", &ptr->id);  // Added & and removed \n
        printf("Temperature: ");
        scanf("%f", &ptr->temp);  // Added & and removed \n
        ptr++;
    }
    
    // Reset pointer to beginning
    ptr = s1;
    
    printf("\n--- Sensor Data ---\n");
    for(int i = 0; i < n; i++){
        printf("Sensor ID: %d, Temperature: %.2f\n", ptr->id, ptr->temp);
        ptr++;
    }
    
    free(s1);  // Free allocated memory
    system("pause");
    return 0;
}