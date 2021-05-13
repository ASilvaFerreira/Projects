
#include <Stepper.h>
#include <LiquidCrystal_I2C.h>

int stepsPerRevolution = 2048;
int rotSpeed = 15;
int rotDir = 1;
Stepper myStepper(2048,8,10,9,11);


int buttonPin = 2;

int buttonValNew;
int buttonValOld = 0;

#define adress 0x27
#define colunas 16
#define linhas 2

LiquidCrystal_I2C lcd(adress,colunas,linhas); 

void setup() {
  
  lcd.init();
  lcd.clear();
  lcd.backlight();
  lcd.print("Rot Direction");
  

  pinMode(buttonPin,INPUT);
  
  myStepper.setSpeed(rotSpeed);
  
}

void loop() {
  buttonValNew = digitalRead(buttonPin);

  if(buttonValOld == 0 && buttonValNew == 1){
    rotDir = rotDir*(-1);
  }
  
  if (rotDir == 1){
    lcd.setCursor(0,1);
    lcd.print("Forward");
  } else {
    lcd.setCursor(0,1);
    
    lcd.print("Backwards");
  }
  
  buttonValOld = buttonValNew;
  
  myStepper.step(rotDir*1);

}
