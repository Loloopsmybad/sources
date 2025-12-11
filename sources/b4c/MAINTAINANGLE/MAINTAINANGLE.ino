#include "Wire.h"
#include <MPU6050_light.h>

MPU6050 mpu(Wire);
unsigned long timer = 0;

int in1=4;//MOTOR 4
int in2=5;//MOTOR 4
int in3=6;//MOTOR 3
int in4=7;//MOTOR 3
int in5=8;//MOTOR 2
int in6=9;//MOTOR 2
int in7=10;//MOTOR 1
int in8=11;//MOTOR  1
int ep1 = 3;//motor1

float anglerequired = 0;
float anglecurrent = 0;
void Forward();
void Backward();
void Right();
void Left();
void Stop();

int distance[10]    = {5000,  5000, 5000, 5000,   5000,5000,5000,5000,5000,5000};
int orientation[10] = {   0,    90,  180,  270, 360,0,0,0,0,0};
int speed = 50;

void setup()
{
  Serial.begin(2000000);
  Wire.begin();
  
  byte status = mpu.begin();
  Serial.print(F("MPU6050 status: "));
  Serial.println(status);
  while(status!=0){ }
  
  Serial.println(F("Calculating offsets, do not move MPU6050"));
  delay(1000);
  mpu.calcOffsets();
  Serial.println("Sensor Init Done!\n");

  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(in5, OUTPUT);
  pinMode(in6, OUTPUT);
  pinMode(in7, OUTPUT);
  pinMode(in8, OUTPUT);
/*
  for(int i=0;i<10;i++)
  {
    Serial.println("Go");
    anglerequired = orientation[i];
    for(int travel = 0;travel < distance[i];)
    {
      mpu.update();	
      anglecurrent = mpu.getAngleZ();
      float error = (anglerequired - anglecurrent);
      float errormod = error*10;
      if(errormod < 0)errormod = -errormod;
      if(errormod > 255)errormod = 255;

      if((error < 3 && (error > -3)){Forward(); analogWrite(ep1,speed);travel++;}
      else if(error < 0){Right(); analogWrite(ep1,errormod);}
      else if(error > 0){Left();analogWrite(ep1,errormod);}  

      Serial.println(error);
    }
    Serial.println("Done");
  }*/
}

void loop() 
{

   for(int i=0;i<10;i++)
  {
    Serial.println("Go");
    anglerequired = orientation[i];
    for(int travel = 0;travel < distance[i];)
    {
      mpu.update();	
      anglecurrent = mpu.getAngleZ();
      float error = (anglerequired - anglecurrent);
      float errormod = error*10;
      if(errormod < 0)errormod = -errormod;
      if(errormod > 255)errormod = 255;

      if((error < 1) && (error > -1)){Forward(); analogWrite(ep1,speed);travel++;}
      else if(error < 0){Right(); analogWrite(ep1,errormod);}
      else if(error > 0){Left();analogWrite(ep1,errormod);}  

      Serial.println(error);
    }
    Serial.println("Done");
  }
}

void Forward()
{
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);  
  digitalWrite(in5,LOW);
  digitalWrite(in6,HIGH);
  digitalWrite(in7,LOW);
  digitalWrite(in8,HIGH);  
}    
void Backward()
{
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  digitalWrite(in5,HIGH);
  digitalWrite(in6,LOW);
  digitalWrite(in7,HIGH);
  digitalWrite(in8,LOW);
}
void Right()
{
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);    
  digitalWrite(in5,HIGH);
  digitalWrite(in6,LOW);
  digitalWrite(in7,LOW);
  digitalWrite(in8,HIGH);
}
void Left()
{
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);    
  digitalWrite(in5,LOW);
  digitalWrite(in6,HIGH);
  digitalWrite(in7,HIGH);
  digitalWrite(in8,LOW);
}
void Stop()
{
  digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,LOW);
  digitalWrite(in5,LOW);
  digitalWrite(in6,LOW);
  digitalWrite(in7,LOW);
  digitalWrite(in8,LOW);    
}

