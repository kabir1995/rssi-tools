/*
  ESP8266 / ESP32 RSSI Measuring tool
*/

// works better on the ESP32

// please define which ESP is being used 
#define ESP32       //uncomment this line if ESP32
//#define ESP8266     //uncomment this line if ESP8266

#ifdef ESP8266
#include <ESP8266WiFi.h>
#endif

#ifdef ESP32
#include <WiFi.h>
#endif

// Replace with your network credentials
const char* ssid     = "ESP-Access-Point";
const char* password = "password1234";

void setup()
{
  Serial.begin(115200);
  // Connect to Wi-Fi network with SSID and password
  Serial.print("Setting AP (Access Point)…");
  boolean result = WiFi.softAP(ssid, password);
  
  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);
}

void loop()
{
  #ifdef ESP8266
  Serial.printf("Stations connected = %d\n", WiFi.softAPgetStationNum());
  #endif
  delay(3000);
}
