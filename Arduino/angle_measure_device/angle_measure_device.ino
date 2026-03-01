
#include <Wire.h>    //Include wire library 
#include <MPU6050_light.h>  //Include library for MPU communication
 //Library for LCD Display

MPU6050 mpu(Wire);   //Create object mpu
    //Define LCD address and dimension

unsigned long timer = 0;    

void setup() {

  Serial.begin(9600);    //Start serial communication

  Wire.begin();     
  mpu.begin();     
 
  delay(1000);
  mpu.calcGyroOffsets();     //Calibrate gyroscope
  Serial.println("Done!\n");

}
void loop() {
    Serial.println("Done!\n");
  mpu.update();    //Get values from MPU
  Serial.print(int(mpu.getAngleZ()));

}