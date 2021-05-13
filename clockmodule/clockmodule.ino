#include <virtuabotixRTC.h>

virtuabotixRTC myRTC(6,7,8);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //myRTC.setDS1302Time(15,7,14,1,26,4,2021);
}

void loop() {
  // put your main code here, to run repeatedly:
  myRTC.updateTime();
  Serial.print("Current date/time: ");
  Serial.print(myRTC.dayofmonth);
  Serial.print("/");
  Serial.print(myRTC.month);
  Serial.print("/");
  Serial.print(myRTC.year);
  Serial.print(" ");
  Serial.print(myRTC.hours);
  Serial.print(":");
  Serial.print(myRTC.minutes);
  Serial.print(":");
  Serial.println (myRTC.seconds);  

  delay(1000);
}
