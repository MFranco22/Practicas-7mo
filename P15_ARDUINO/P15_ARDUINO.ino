#include<WiFi.h>
const char* ssid="informatica7";
const char* password="Info_@@7";
WiFiServer serve(12345);
WiFiClient cliente;
void setup() {

Serial.begin(115200);
WiFi.begin(ssid,password);
while( WiFi.status()!= WL_CONNECTED){
delay(1000);
Serial.println("Conectandose..........");

}
Serial.println("cliente conectado");
Serial.println(WiFi.localIP());
serve.begin();
}

void loop() {
int g = random(0,255);
if(!cliente || !cliente.connected()) {
  cliente = serve.available();
}
cliente.println(g);
delay(1000);



}