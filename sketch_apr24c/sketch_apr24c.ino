#include <Servo.h>
const int left = 9;
const int right = 2;
const int servoPin = 10;

int servoPos = 50;
int rotStep = 2;
int leftState = 0;
int rightState = 0;

Servo myServo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(left,INPUT);
  pinMode(right, INPUT);
  
  myServo.attach(servoPin);
}

void loop() {
  // put your main code here, to run repeatedly:
  leftState = digitalRead(left);
  rightState = digitalRead(right);
  if (leftState == 1 and servoPos < 180){
    servoPos += rotStep;
    Serial.print("Servo Position set to ");
    Serial.println(servoPos);
    myServo.write(servoPos);
    delay(50);
  }
  if (rightState ==1 and servoPos > 0) {
    servoPos -= rotStep;
    Serial.print("Servo Position set to ");
    Serial.println(servoPos);
    myServo.write(servoPos);
    delay(50);
  }
  myServo.write(servoPos);
}
