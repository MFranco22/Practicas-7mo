
#include<WiFi.h>
const char* ssid = "informatica7";
const char*  password="Info_@@7";
WiFiServer serve(12345);
WiFiClient cliente;
#define btn 5
#define led 4
#define ledi 2
#define b 18

int con = 0;

void setup() {
  pinMode(btn, INPUT);
  pinMode(led, OUTPUT);
  pinMode(ledi, OUTPUT);
  pinMode(b, OUTPUT);
  Serial.begin(115200);
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("Conectandose....");
  }
  Serial.println("Cliente conectado");
  Serial.println(WiFi.localIP());
  serve.begin();  
  digitalWrite(ledi,HIGH);
}

void loop() {
 
  if (!cliente || !cliente.connected()){
    cliente = serve.available();
  }

  int estado = digitalRead(btn);
  delay(500);
  
 if (estado== 1 && con == 0){
  Serial.print("Boton: ");
  Serial.println(estado);
  digitalWrite(ledi,LOW);
  digitalWrite(led,HIGH);
  con = 1;
  //tone(b,500);
  delay(500);
  return;
 }
 //delay(500);
 if (estado == 1 && con > 0){
  cliente.println(String(con));
  tone(b,500);
  con++;
  Serial.print("Enviamos: ");
  Serial.println(con);
   if (con>=6){
    con = 0;
    estado = 0;
    //cliente.close();
    digitalWrite(led,LOW);
    digitalWrite(ledi,HIGH);
   }
   delay(300);
 }
 noTone(b);
}







