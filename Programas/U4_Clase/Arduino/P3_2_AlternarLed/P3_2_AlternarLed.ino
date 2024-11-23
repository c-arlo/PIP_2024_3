int led1 = 13; // led pin 13 positivo y GND (Ground) negativo
int led2 = 2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // estandar 9600 siempre
  pinMode(led1,OUTPUT); // indicar que pin se va a utilizar y de que forma se utilizara
  pinMode(led2,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("LED 1 ON / LED 2 OFF");
  digitalWrite(led1,HIGH);
  delay(3000);
  Serial.println("LED 1 OFF / LED 2 OFF");
  digitalWrite(led1,LOW);
  delay(1000);
  Serial.println("LED 1 OFF / LED 2 ON");
  digitalWrite(led2,HIGH);
  delay(5000);
  Serial.println("LED 1 OFF / LED 2 OFF");
  digitalWrite(led2,LOW);
  delay(1000);
}
