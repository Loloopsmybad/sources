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
void SlideLeft();
void SlideRight();
void GoForward(int distance,int orientation ,int speed);

void setup()
{
  //Serial.begin(2000000);
  Wire.begin();
  
  byte status = mpu.begin();
  //Serial.print(F("MPU6050 status: "));
  //Serial.println(status);
  while(status!=0){ }
  
  //Serial.println(F("Calculating offsets, do not move MPU6050"));
  delay(1000);
  mpu.calcOffsets();
  //Serial.println("Sensor Init Done!\n");

  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(in5, OUTPUT);
  pinMode(in6, OUTPUT);
  pinMode(in7, OUTPUT);
  pinMode(in8, OUTPUT);

  GoForward(300,0,150);
   GoForward(1,45,150);
   GoLeft(40,45,255);
  GoForward(250,45,150);
  GoForward(1,90,150);
    GoLeft(80,90,255);
  
  GoForward(500,90,150);
  GoForward(0,180,90);
  GoLeft(100,180,255);
  GoForward(490,180,150);
  GoForward(1,315,150);

  GoLeft(110,315,255);
  GoBk(300,315,255);
  GoForward(1000,315,255);
  GoBk(1000,315,255);
  GoForward(1000,315,255);
  GoBk(1000,315,150);
  GoForward(1000,315,255);

  GoForward(1,450,150);
  GoLeft(250,450,255);
  GoForward(900,450,150); 
  GoForward(1,540,150);
  GoLeft(200,540,255);
  GoBk(150,540,150);
  GoForward(900,540,150);
  GoForward(1,630,150);
  GoLeft(200,630,255);
  GoBk(150,630,150);
  GoForward(900,630,150);

   





  Stop();
}

void loop() {}

void GoForward(int distance,int orientation, int speed)
{
    anglerequired = -orientation;
    for(int travel = 0;travel < distance;)
    {
      mpu.update();	
      anglecurrent = mpu.getAngleZ();
      float error = (anglerequired - anglecurrent);
      float errormod = error*30;
      if(errormod < 0)errormod = -errormod;
      if(errormod > 255)errormod = 255;

      if((error < 3) && (error > -3)){Forward(); analogWrite(ep1,speed);travel++;}
      else if(error < 0){RotateRight(); analogWrite(ep1,errormod);}
      else if(error > 0){RotateLeft();analogWrite(ep1,errormod);}  
    }
}
void GoBk(int distance,int orientation, int speed)
{
    anglerequired = -orientation;
    for(int travel = 0;travel < distance;)
    {
      mpu.update();	
      anglecurrent = mpu.getAngleZ();
      float error = (anglerequired - anglecurrent);
      float errormod = error*30;
      if(errormod < 0)errormod = -errormod;
      if(errormod > 255)errormod = 255;

      if((error < 3) && (error > -3)){Backward(); analogWrite(ep1,speed);travel++;}
      else if(error < 0){RotateRight(); analogWrite(ep1,errormod);}
      else if(error > 0){RotateLeft();analogWrite(ep1,errormod);}  
    }
}

void GoLeft(int distance,int orientation ,int speed)
{
    anglerequired = -orientation;
    for(int travel = 0;travel < distance;)
    {
      mpu.update();	
      anglecurrent = mpu.getAngleZ();
      float error = (anglerequired - anglecurrent);
      float errormod = error*30;
      if(errormod < 0)errormod = -errormod;
      if(errormod > 255)errormod = 255;

      if((error < 3) && (error > -3)){SlideLeft(); analogWrite(ep1,speed);travel++;}
      else if(error < 0){RotateRight(); analogWrite(ep1,errormod);}
      else if(error > 0){RotateLeft();analogWrite(ep1,errormod);}  
    }
}
void GoRight(int distance,int orientation, int speed)
{
    anglerequired = -orientation;
    for(int travel = 0;travel < distance;)
    {
      mpu.update();	
      anglecurrent = mpu.getAngleZ();
      float error = (anglerequired - anglecurrent);
      float errormod = error*30;
      if(errormod < 0)errormod = -errormod;
      if(errormod > 255)errormod = 255;

      if((error < 3) && (error > -3)){SlideRight(); analogWrite(ep1,speed);travel++;}
      else if(error < 0){RotateRight(); analogWrite(ep1,errormod);}
      else if(error > 0){RotateLeft();analogWrite(ep1,errormod);}  
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
void RotateRight()
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
void RotateLeft()
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

void SlideLeft()
{
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);  
  digitalWrite(in5,LOW);
  digitalWrite(in6,HIGH);
  digitalWrite(in7,HIGH);
  digitalWrite(in8,LOW);

}
void SlideRight()
{
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  digitalWrite(in5,HIGH);
  digitalWrite(in6,LOW);
  digitalWrite(in7,LOW);
  digitalWrite(in8,HIGH);

}

