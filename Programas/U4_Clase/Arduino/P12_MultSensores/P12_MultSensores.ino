int s1 = A0;
int s2 = A1;
int s3 = A2;
int s4 = A3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int v1, v2, v3, v4;

void loop() {
  // put your main code here, to run repeatedly:
  v1 = analogRead(s1);
  v2 = analogRead(s2);
  v3 = analogRead(s3);
  v4 = analogRead(s4);

  //Opc1
  /*
  Serial.println("S1-" + String(v1));
  Serial.println("S2-" + String(v2));
  Serial.println("S3-" + String(v3));
  Serial.println("S4-" + String(v4));
  */

  //Opc2 - Trama
  Serial.println("A " 
  + String(v1) + "-" 
  + String(v2) + "-" 
  + String(v3) + "-" 
  + String(v4) + " Z");
}
