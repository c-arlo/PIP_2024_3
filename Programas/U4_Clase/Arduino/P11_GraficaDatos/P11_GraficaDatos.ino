int sensor = A0; //sensor analogico fotoresistencia/LDR o potenciometro
void setup() {
  Serial.begin(9600);
}

int valor_sensor;
void loop() {
  valor_sensor = analogRead(sensor);
  Serial.println(valor_sensor);
  delay(1000);
}
