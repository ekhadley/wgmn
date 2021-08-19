#include <ESP8266WiFi.h>

#include <WiFiClientSecure.h>


WiFiClientSecure client;

#define PORT 443

// wifi connection variables
const char* ssid     = "THE LOFT";
const char* password = "perfectpanda699";

boolean wifiConnected = false;

int incomingByte = 0;
boolean connectWifi();

PushBullet pb = PushBullet("o.sWopNdukIljKlWbazQk8Rp2tQwiEdarj", &client, 443);


void setup() {
  // Initialise Serial connection
  Serial.begin(115200);

  // Initialise wifi connection
  wifiConnected = connectWifi();

  if (!pb.checkConnection()) {
    Serial.println("Failed to connect to pushbullet.com");
    return;
  }

}
boolean connectWifi() {
  boolean state = true;
  int i = 0;
  WiFi.begin(ssid, password);
  Serial.println("");
  Serial.println("Connecting to WiFi");

  // Wait for connection
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    if (i > 10) {
      state = false;
      break;
    }
    i++;
  }
  if (state) {
    Serial.println("");
    Serial.print("Connected to ");
    Serial.println(ssid);
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
  }
  else {
    Serial.println("");
    Serial.println("Connection failed.");
  }
  return state;
}

void loop() {
  if (wifiConnected){
    delay(5000);
    Serial.println("Pushbullet note pushing");
    pb.sendNotePush("yo", "Message");
   
    
  }
}
