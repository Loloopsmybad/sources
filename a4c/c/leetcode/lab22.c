#include<stdlib.h>
#include<stdio.h>

struct sensor{
	int sno;
	int id;
	float temp;
	struct sensor *next;

};
struct sensor *s;
void addnode(){ 
			
                struct sensor *s = (struct sensor *)malloc(sizeof(struct sensor));
                printf("Enter data for sensor : ");
                scanf("%d\n",&s->sno);
                printf("Sensor ID:");
                scanf("%d\n",&s->id);
                printf("Temperature:");
                scanf("%f\n",&s->temp);
             
}

int main(){
	int a=0;
	int head2=0;
	struct sensor *head;
	printf("number of sensor ");
	scanf("%d",&a);
	for(int i=1;i<=a;i++){
		if(head2==0){
                        hiead=s;
                        }
		if (head2>0){
                s->next=head;
                }
                else if (head2 =a){
                head->next=NULL;
                }

		addnode();
                head2++;
		}


	float arr[a];
	int i=0;
	struct sensor *it;
	it = head;
	while(it!=NULL){
		arr[i]=it->temp;
		it=it->next;
	}

	int check=0;
	for(int k=0;k<a;k++){
		if (arr[k]>check){
		check=arr[k];
		}
	
	}
	printf("Sensor Readings:\n");
	while (head!=NULL){
		printf("sensor ID : %d,Temperature: %f \n",head->id, head->temp);
		head=head->next;
	
	}
	printf("Maximum Temperature: %d",check);


	return 0;
}


