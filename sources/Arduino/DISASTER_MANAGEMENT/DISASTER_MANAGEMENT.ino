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

  GoForward(550,0,200); 
  GoBk(150,0,190);
  //GoLeft(100,0,190);



  GoLeft(180,90,255);
  GoForward(500,90,190);
  GoBk(200,90,190);


  
  //GoLeft(0,180,200);
  GoRight(180,180,200);
  GoForward(800,180,190); 
  GoBk(100,180,190);
  
  
  GoRight(290,270,200);  
  GoForward(290,270,190);
  //GoBk(200,270,190);
  
  GoLeft(100,360,200);  
  GoForward(400,360,190);


  GoRight(200,270,255);
  GoForward(500,270,200);

  GoBk(400,270,200);
  GoBk(80,180,200);

  GoLeft(450,180,255);
  GoForward(700,180,200); 

   GoLeft(300,360,255);

   GoForward(400,360,200);
   GoBk(40,270,200);
   GoRight(110,270,255);
   GoForward(600,270,200);

      




  
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

