int led = 13; // led pin 13 positivo y GND (Ground) negativo
int v;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // estandar 9600 siempre
  pinMode(led,OUTPUT); // indicar que pin se va a utilizar y de que forma se utilizara
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led,HIGH);
  Serial.println("Led encendido");
  delay(1000);
  digitalWrite(led,LOW);
  Serial.println("Led apagado");
  delay(1000);
}
