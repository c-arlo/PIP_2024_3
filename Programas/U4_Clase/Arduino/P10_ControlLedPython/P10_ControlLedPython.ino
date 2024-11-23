int led = 13;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
  pinMode(led,OUTPUT);
}

void loop() {
  if(Serial.available()>0) {
    int r = Serial.readString().toInt();
    digitalWrite(led,r);
  }
  delay(10);
}
