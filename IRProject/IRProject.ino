#include "buttonMapping.h"
#include <IRremote.h>
#include <Servo.h>
int IRpin = 12;
IRrecv irrecv(IRpin);
decode_results results;

const int led1 = 8;
const int led2 = 9;
const int led3 = 10;
const int buzzer = 4;
const int servoPin = 11;
int servoPos = 50;

int rotStep = 10;

int itsONled[] = {0,0,0,0};
int buzzState = 0;

Servo myServo;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  irrecv.enableIRIn(); 

  myServo.attach(servoPin);
  
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (irrecv.decode(&results)) {
    unsigned int value = results.value;
    switch (value) {
      case button1:
        if (itsONled[1] == 1) {
          digitalWrite(led1, LOW);
          itsONled[1] = 0;
        } else {
          digitalWrite(led1,HIGH);
          itsONled[1] = 1;
        }
        break;
      case button2:
        if (itsONled[2] == 1) {
          digitalWrite(led2, LOW);
          itsONled[2] = 0;
        } else {
          digitalWrite(led2,HIGH);
          itsONled[2] = 1;
        }
        break;
      case button3:
        if (itsONled[3] == 1) {
          digitalWrite(led3, LOW);
          itsONled[3] = 0;
        } else {
          digitalWrite(led3,HIGH);
          itsONled[3] = 1;
        }
        break;
      case buttonEQ:
        if( buzzState == 0){
          tone(buzzer, 200);
        } else {
        noTone(buzzer);
        }
        break;
        
      case buttonPrev:
        servoPos -= rotStep;
        Serial.print("Servo Position set to ");
        Serial.println(servoPos);
        myServo.write(servoPos);
        delay(50);


      case buttonNext:
        servoPos += rotStep;
        Serial.print("Servo Position set to ");
        Serial.println(servoPos);
        myServo.write(servoPos);
        delay(50);

    }
    Serial.println(value,DEC);
    irrecv.resume();
  }
}
