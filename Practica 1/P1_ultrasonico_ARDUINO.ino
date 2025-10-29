#define trig 25  // Pin de salida (TRIG) del sensor
#define echo 33  // Pin de entrada (ECHO) del sensor

// Variable para guardar la distancia calculada
float dist;

void setup() {
  // Iniciamos la comunicación serial para ver datos en el monitor
  Serial.begin(115200);

  // Configuramos los pines: TRIG como salida, ECHO como entrada
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);

  // Mensaje inicial en el monitor serial
  Serial.println("ESP32");
}

void loop() {
  // Preparamos el TRIG: lo apagamos brevemente
 // digitalWrite(trig, LOW);
 // delayMicroseconds(2);

  // Enviamos un pulso ultrasónico de 10 microsegundos
 // digitalWrite(trig, HIGH);
 // delayMicroseconds(10);
 // digitalWrite(trig, LOW);

  // Medimos el tiempo que tarda en regresar el eco (en microsegundos)
  //dist = pulseIn(echo, HIGH);

  // Convertimos ese tiempo a distancia en centímetros
  // Fórmula: distancia (cm) = tiempo (µs) / 58
  //dist = dist / 58;
  dist = random(1,100);

  // Mostramos la distancia en el monitor serial
  //Serial.print("Distancia: ");
  Serial.println(dist);
  //Serial.println("cm");

  // Esperamos medio segundo antes de la siguiente lectura
  delay(1000);
}