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

//String incoming;
//  if (Serial.available() > 0) {
//    // read the incoming:
//    incoming = Serial.readString();
//    // say what you got:
//    ssid = incoming.c_str();
//    Serial.println(ssid);
//  }

void setup() {
  Serial.begin(115200);
  connectWiFi();
}

void loop() {
  int wifiStrength;
  int delay_time = 20;
      
  if (WiFi.status() != WL_CONNECTED) { 
      connectWiFi();
  }

  wifiStrength = WiFi.RSSI(); 
  delay(delay_time);
  Serial.println(wifiStrength);
}

void connectWiFi(){
  while (WiFi.status() != WL_CONNECTED){
      WiFi.begin(ssid, password);
      Serial.print(".");
      delay(3000);
  }
  Serial.println("Connected");
}
