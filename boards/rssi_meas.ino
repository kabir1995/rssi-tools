#include <WiFi.h>

char* ssid = "Rodrigo's iPhone";
const char* password = "12345678";

void setup() {
  Serial.begin(115200);
  connectWiFi();
}

void loop() {
    int wifiStrength;

    if (WiFi.status() != WL_CONNECTED) { 
        connectWiFi();
    }

    wifiStrength = WiFi.RSSI(); 

    Serial.println(wifiStrength);
}

void connectWiFi(){
    while (WiFi.status() != WL_CONNECTED){
        WiFi.begin(ssid, password);
        delay(3000);
    }
    Serial.println("Connected");
}