

#include <Wire.h>     // include Arduino Wire library
#include "rgb_lcd.h"
#include <Servo.h>
#include "Wire.h"
#include <MPU6050_light.h>




Servo servo_9;
int a=0;

rgb_lcd lcd; 


MPU6050 mpu(Wire);
unsigned long timer = 0;
int a =0;
int in1=4;//MOTOR 4
int in2=5;//MOTOR 4
int in3=6;//MOTOR 3
int in4=7;//MOTOR 3
int in5=8;//MOTOR 2
int in6=9;//MOTOR 2
int in7=10;//MOTOR 1
int in8=11;//MOTOR  1

int ep1 = 3;//motor1



void setup() {
  Serial.begin(9600);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(in5, OUTPUT);
  pinMode(in6, OUTPUT);
  pinMode(in7, OUTPUT);
  pinMode(in8, OUTPUT);
  Wire.begin();
  status = mpu.begin();
  lcd.begin(16, 2);

  // move cursor to upper left position (0, 0)
  lcd.setCursor(0, 0);

  // print text on the LCD
  lcd.print("lolololol");

  char txt[] = "                Ready for nationals \0";

  lcd.setCursor(0, 1);  // move cursor to second row
  lcd.print(txt);  
    
      while(txt[0] != '\0')
  {
    byte i = 0;
    lcd.setCursor(0, 1);
    while(txt[i] != '\0') // shift the text array to the left by 1 position
    {
      lcd.write(txt[i]);  // print one character
      txt[i] = txt[i+1];  // shift the text array to the left
      i++;
    }

    lcd.write(' ');  // print a space
    delay(200);      // wait 200 milliseconds
  }



   

}





void loop() {
  mpu.update();
  a= mpu.getAngleZ();
  serial.print(a);
  while (int i ; i<10; i++;){

    serial.print(int(mpu.getAngleZ()));
  }

delay(200000);


}

 