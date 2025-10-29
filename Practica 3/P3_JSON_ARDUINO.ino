//Instalar la libreria de ArduinoJson

#include<ArduinoJson.h>

void setup() {
  Serial.begin(115200);
}

void loop() {
  StaticJsonDocument<100> doc; //parametro de los que van a caber en el doc

  JsonArray labels = doc.createNestedArray("labels");
  labels.add("A");
  labels.add("B");
  labels.add("C");

  JsonArray values = doc.createNestedArray("values");
  values.add(random(20,100));
  values.add(random(20,100));
  values.add(random(20,100));

  serializeJson(doc, Serial);
  Serial.println();
  delay(1000);


}
