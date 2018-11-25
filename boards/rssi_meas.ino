/*
  ESP8266 / ESP32 RSSI Measuring tool
*/

//  works better on the ESP8266   

// please define which ESP is being used 
//#define ESP32       //uncomment this line if ESP32
#define ESP8266     //uncomment this line if ESP8266

#ifdef ESP8266
#include <ESP8266WiFi.h>
#endif

#ifdef ESP32 
#include <WiFi.h>
#endif

const char* ssid = "ESP-Access-Point";
const char* password = "password1234";

char incoming;
bool flag;

void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  connectWiFi();
}

void loop() {
  int wifiStrength;
  int delay_time = 20;
      
  if (WiFi.status() != WL_CONNECTED) { 
      connectWiFi();
  }

  if (Serial.available() > 0) {
    incoming = Serial.read();
    if (incoming == 0x41){
      Serial.println(0x61);
      flag = true;
    }
  }
  while(flag){
    wifiStrength = WiFi.RSSI(); 
    delay(delay_time);
    Serial.println(wifiStrength);
    if (Serial.available() > 0) {
      incoming = Serial.read();
      if (incoming == 0x41){
        Serial.println(0x61);
        flag = true;
      }
      if (incoming == 0x51){
        Serial.println(0x71);
        flag = false;
      }
    }
  }
}

void connectWiFi(){
  while (WiFi.status() != WL_CONNECTED){
      WiFi.begin(ssid, password);
      digitalWrite(LED_BUILTIN, HIGH); 
      delay(750);                       
      digitalWrite(LED_BUILTIN, LOW);   
      delay(750);  
      digitalWrite(LED_BUILTIN, HIGH); 
      delay(750);                       
      digitalWrite(LED_BUILTIN, LOW);   
      delay(750);  
  }
  digitalWrite(LED_BUILTIN, LOW);   
}
