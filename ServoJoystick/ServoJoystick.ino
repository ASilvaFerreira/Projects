#include <Servo.h>


const int servoPin = 11;
const int led1 = 10;
const int led2 = 8;
const int led3 = 9;

int joyX = 0;
int joyY = 1; 

Servo myServo;

int joyVal;

void setup() {
  // put your setup code here, to run once:
  myServo.attach(servoPin);
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
}

void loop() {
   joyVal = analogRead(joyX);
   joyVal = map( joyVal, 0, 1023 , 0, 180);


   myServo.write(joyVal);

  if ( joyVal > 80 and joyVal < 100) {
    digitalWrite(led1,HIGH);
  } else {
    digitalWrite(led1,LOW);
  }

  if ( joyVal < 15) {
    digitalWrite(led2,HIGH);
  } else {
    digitalWrite(led2,LOW);
  }

    if ( joyVal > 170) {
    digitalWrite(led3,HIGH);
  } else {
    digitalWrite(led3,LOW);
  }
}
