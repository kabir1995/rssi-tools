#include <WiFi.h>

char* ssid = "ruanito";
const char* password = "fratagay";

int measurementNumber = 0;

void setup() {
  Serial.begin(115200);
  connectWiFi();
}

// the loop function runs over and over again forever
void loop() {
    const int numberPoints = 1;
    float wifiStrength;

    if (WiFi.status() != WL_CONNECTED) { 
        connectWiFi();
    }

    wifiStrength = getStrength(numberPoints); 
    measurementNumber++;

    Serial.println(wifiStrength);
}

void connectWiFi(){

    while (WiFi.status() != WL_CONNECTED){
        WiFi.begin(ssid, password);
        delay(3000);
    }

    // Show the user a connection is successful.
    Serial.println("Connected");
}

int getStrength(int points){
    long rssi = 0;
    long averageRSSI=0;
    
    for (int i=0;i < points;i++){
        rssi += WiFi.RSSI();
        delay(80);
    }

    averageRSSI=rssi/points;
    return averageRSSI;
}
