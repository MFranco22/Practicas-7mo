#include<ArduinoJson.h>
bool ban= false;

void setup() {
//habilitamos serial
Serial.begin (115200);
}

void loop() {
  //numero de datos que se pueden aguardar
StaticJsonDocument<100> doc;

//definimos valores
if(ban){
int valor1= random (1,100);
int valor2= random (1,100);
JsonArray labels = doc.createNestedArray("labels");
labels.add("valor1");
labels.add("valor2");
JsonArray values = doc.createNestedArray("values");
values.add(valor1);
values.add(valor2);
serializeJson(doc,Serial);
Serial.println();
}
if(Serial.available()){
  char c = Serial.read();
    if (c == '1'){
      ban = !ban;

    } 
    
  }
delay(1000);
}