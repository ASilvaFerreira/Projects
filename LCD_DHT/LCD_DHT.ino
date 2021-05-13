
// INCLUSÃO DE BIBLIOTECAS
#include <DHT.h>

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// DEFINIÇÕES
#define DHTPIN 2
#define DHTTYPE DHT11


#define endereco  0x27 // Endereços comuns: 0x27, 0x3F
#define colunas   16
#define linhas    2

// INICIAR OBJETOS
DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(endereco, colunas, linhas);

void setup() {
  // put your setup code here, to run once:
  dht.begin();

  lcd.init(); // INICIA A COMUNICAÇÃO COM O DISPLAY
  lcd.backlight(); // LIGA A ILUMINAÇÃO DO DISPLAY
  lcd.clear(); // LIMPA O DISPLAY

  lcd.setCursor(0,0);
  lcd.print("H:");
  lcd.setCursor(0,1);
  lcd.print("T:");
}

void loop() {
  // put your main code here, to run repeatedly:
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  lcd.setCursor(3,0);
  lcd.print(h);
  
  lcd.setCursor(3,1);
  lcd.print(t);
  
  delay(1000);
}
