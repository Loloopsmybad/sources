#include <Stepper.h>

// change this to the number of steps on your motor
const int STEPS=20;

// create an instance of the stepper class, specifying
// the number of steps of the motor and the pins it's
// attached to
Stepper stepper(STEPS, 8, 9, 10, 11);
Stepper stepper2(STEPS, 4, 5, 6, 7);

// the previous reading from the analog input
int previous = 0;

void setup() {
  // set the speed of the motor to 30 RPMs
  stepper.setSpeed(5);
  stepper2.setSpeed(5);
  Serial.begin(9600);
}

void loop() {
  // get the sensor value
  //int val = analogRead(0);

  //int step=map(val, 0, 1023, 0, STEPS);
  
  stepper.step(STEPS);

  stepper2.step(STEPS);
  
  
  // move a number of steps equal to the change in the
  // sensor reading
  //stepper.step(val - previous);

  // remember the previous value of the sensor
  //previous = val;
}
 