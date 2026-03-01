/* Get tilt angles on X and Y, and rotation angle on Z
 * Angles are given in degrees
 * 
 * License: MIT
 */

#include <Wire.h>     // include Arduino Wire library
#include "rgb_lcd.h"

#include "Wire.h"
#include <MPU6050_light.h>

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
  byte status = mpu.begin();
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

 

  Wire.begin();
  
  status = mpu.begin();
  Serial.print(F("MPU6050 status: "));
  Serial.println(status);
  while(status!=0){ } // stop everything if could not connect to MPU6050
  
  Serial.println(F("Calculating offsets, do not move MPU6050"));
  delay(1000);
  mpu.upsideDownMounting = true; // uncomment this line if the MPU6050 is mounted upside-down
  mpu.calcOffsets(); // gyro and accelero
  Serial.println("Done!\n");
}

void loop() {
  mpu.update();
  a= mpu.getAngleZ();
  Serial.print("lmao");
  Serial.print(a);
  for (int i=0 ; i<10; i++){
     Serial.print(int(mpu.getAngleZ()));

  }

  delay(100000);

}
