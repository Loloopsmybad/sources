const int trigPin = 3;//3
const int echoPin = 2;//2
const int trigPin2 = 5;
const int echoPin2 = 4;
const int trigPin3 = 7;
const int echoPin3 = 6;
const int trigPin4 = A5;
const int echoPin4 = A4;

const int sensor1 = A0;
const int sensor2 = A1;
const int sensor3 = A2;
const int sensor4 = A3;
const int led_u = 8;
const int led_1 = 9;
const int led_2 = 10;
const int led_3 = 11;
const int led_4 = 12;

int sen = 0;
int sen2 = 0;
int sen3 = 0;
int sen4 = 0;

int a;
int diff_dist;
int diff_dist2;
long duration1;
long duration2;
long duration3;
long duration4;
int distance1;
int distance2;
int distance3;
int distance4;


 
void setup()
{
    pinMode(sensor1, INPUT);
    pinMode(sensor2, INPUT);
    pinMode(sensor3, INPUT);
    pinMode(sensor4, INPUT);
    pinMode(led_u, OUTPUT);
    pinMode(led_1, OUTPUT);
    pinMode(led_2, OUTPUT);
    pinMode(led_3, OUTPUT);
    pinMode(led_4, OUTPUT);
    pinMode(trigPin,OUTPUT); 
    pinMode(echoPin, INPUT); 
    pinMode(trigPin2,OUTPUT);
    pinMode(echoPin2, INPUT);
    pinMode(trigPin3,OUTPUT);
    pinMode(echoPin3, INPUT);
    pinMode(trigPin4,OUTPUT);
    pinMode(echoPin4, INPUT);
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
}
 
void loop()
{
  /*
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2); // wait for 2 ms to avoid
    digitalWrite(trigPin, HIGH); // turn on the Trigger to generate pulse
    delayMicroseconds(10); // keep the trigger "ON" for 10 ms to generate
    digitalWrite(trigPin,LOW); // Turn off the pulse trigger to stop
    duration1 = pulseIn(echoPin, HIGH);
    distance1 = duration1 * 0.0344 / 2; // Expression to calculate
    Serial.print("Distance1: ");
    Serial.print(distance1); // Print the output in serial monitor
    Serial.println(" cm");
    
    
        digitalWrite(trigPin2, LOW);
    delayMicroseconds(2); // wait for 2 ms to avoid
    digitalWrite(trigPin2, HIGH); // turn on the Trigger to generate pulse
    delayMicroseconds(10); // keep the trigger "ON" for 10 ms to generate
    digitalWrite(trigPin2,LOW); // Turn off the pulse trigger to stop
    duration2 = pulseIn(echoPin2, HIGH);
    distance2 = duration2 * 0.0344 / 2; // Expression to calculate
    Serial.print("Distance2: ");
    Serial.print(distance2); // Print the output in serial monitor
    Serial.println(" cm");


      
        digitalWrite(trigPin3, LOW);
    delayMicroseconds(2); // wait for 2 ms to avoid
    digitalWrite(trigPin3, HIGH); // turn on the Trigger to generate pulse
    delayMicroseconds(10); // keep the trigger "ON" for 10 ms to generate
    digitalWrite(trigPin3,LOW); // Turn off the pulse trigger to stop
    duration3 = pulseIn(echoPin3, HIGH);
    distance3 = duration3 * 0.0344 / 2; // Expression to calculate
    Serial.print("Distance3: ");
    Serial.print(distance3); // Print the output in serial monitor
    Serial.println(" cm");
    
        digitalWrite(trigPin4, LOW);
    delayMicroseconds(2); // wait for 2 ms to avoid
    digitalWrite(trigPin4, HIGH); // turn on the Trigger to generate pulse
    delayMicroseconds(10); // keep the trigger "ON" for 10 ms to generate
    digitalWrite(trigPin4,LOW); // Turn off the pulse trigger to stop
    duration4 = pulseIn(echoPin4, HIGH);
    distance4 = duration4 * 0.0344 / 2; // Expression to calculate
    Serial.print("Distance4: ");
    Serial.print(distance4); // Print the output in serial monitor
    Serial.println(" cm");
    
    */
  /*  
    digitalWrite(trigPin2, LOW);
    delayMicroseconds(2); // wait for 2 ms to avoid
    digitalWrite(trigPin2, HIGH); // turn on the Trigger to generate pulse
    delayMicroseconds(10); // keep the trigger "ON" for 10 ms to generate
    digitalWrite(trigPin2,LOW); // Turn off the pulse trigger to stop
    duration2 = pulseIn(echoPin2, HIGH);
    distance2 = duration2 * 0.0344 / 2; // Expression to calculate
   // Serial.print("Distance: ");
   // Serial.print(distance2); // Print the output in serial monitor
   // Serial.println(" cm");  


*/

  sen = analogRead(sensor1);
  if (sen > 200) {
    digitalWrite(led_1, LOW);
  } else {
    digitalWrite(led_1, HIGH);
  }


  sen2 = analogRead(sensor2);
  if (sen2 >500) {
    digitalWrite(led_2, LOW);
  } else {
    digitalWrite(led_2, HIGH);
  }
 

  sen3 = analogRead(sensor3);
  if (sen3 > 200) {
    digitalWrite(led_3, LOW);
  } else {
    digitalWrite(led_3, HIGH);
  }

  sen4 = analogRead(sensor4);
  if (sen4 > 400) {
    digitalWrite(led_4, LOW);
  } else {
    digitalWrite(led_4, HIGH);
  }


  if (sen > 200 && sen2 > 200 && sen3 > 200 && sen4 > 250) {

    digitalWrite(led_u, HIGH);
  }
  else {
    digitalWrite(led_u, LOW);
  }
   // Wait for 100 millisecond(s)
 /*
  //diff_dist= abs(distance1-distance3);
  diff_dist2= abs(distance2-distance4);
 
      if (diff_dist > 15 ){

          digitalWrite(led_u, HIGH); 
      }else if  (diff_dist < 10 ){
          
          digitalWrite(led_u, LOW); 
      }*/
/*
      if (diff_dist2 > 10 && distance3 > distance4 ){

          digitalWrite(led_2, HIGH); 
      }else if  (diff_dist2 > 10 && distance3 < distance4 ){
          
          digitalWrite(led_4, HIGH); 
      }
*/

 /*
 if (distance1 < 20 ) {
      digitalWrite(led_u, HIGH);  // turn the LED on (HIGH is the voltage level)
                         // wait for a second
    }
    else{
      digitalWrite(led_u, LOW);   // turn the LED off by making the voltage LOW
    }

    if (distance2 < 10 ) {
      digitalWrite(led_u, HIGH);  // turn the LED on (HIGH is the voltage level)
                         // wait for a second
    }
    else{
      digitalWrite(led_u, LOW);   // turn the LED off by making the voltage LOW
    }

  
  a = sen+sen2+sen3+sen4;
  diff_dist= abs(distance1-distance2);
  diff_dist2= abs(distance3-distance4);
  if (a = 0){

      if (diff_dist >  && distance1 > distance2 ){

          digitalWrite(led_1, HIGH); 
      }else if  (diff_dist > 5 && distance1 < distance2 ){
          
          digitalWrite(led_3, HIGH); 
      }

      if (diff_dist2 > 5 && distance3 > distance4 ){

          digitalWrite(led_2, HIGH); 
      }else if  (diff_dist2 > 5 && distance3 < distance4 ){
          
          digitalWrite(led_4, HIGH); 
      }
      
  }
 
*/
   

   delay(100);
}