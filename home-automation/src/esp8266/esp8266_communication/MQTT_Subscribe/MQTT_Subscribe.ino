#include <ESP8266WiFi.h>
#include <PubSubClient.h>

Servo myservo;

const char* ssid = "aathi";
const char* password = "00006666";
const char* mqtt_server = "192.168.43.90";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("Time")) {///////////////THIS MUST BE A UNIQUE NAME FOR EACH ESP8266
      //Time
      //Epona
      //SunStormForest
      //Fire
      //Zelda
      Serial.println("connected");
      // Once connected, publish an announcement...
      //client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("ledStatus");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Do the thing if your song plays
  if ((char)payload[0]=='1') {
    digitalWrite(13,HIGH);//storms
  }
  if ((char)payload[0]=='0') {
    digitalWrite(13,LOW);//forest
  }
}
void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  }

void setup() {
  pinMode(13, OUTPUT);// Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  }
}
