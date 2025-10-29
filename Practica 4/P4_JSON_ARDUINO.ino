//Instalar la libreria de ArduinoJson

#include<ArduinoJson.h>
#define po 34

void setup() {
  Serial.begin(115200);
}

void loop() {
  StaticJsonDocument<100> doc; //parametro de los que van a caber en el doc

  doc["Labels"] = "Sensor";
  doc["values"] = random(10,200);

  serializeJson(doc, Serial);
  Serial.println();
  delay(1000);


}
