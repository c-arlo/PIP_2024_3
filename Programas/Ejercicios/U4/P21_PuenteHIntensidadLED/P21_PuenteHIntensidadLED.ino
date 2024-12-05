int ENA = 3;
int in1 = 5;

void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);

  Serial.begin(9600);
  Serial.setTimeout(10);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
      int v = Serial.readString().toInt();      
      digitalWrite(in1, 1); //donde el output 1 esta coenctado a un led      
      analogWrite(ENA, v); //v debe de ir de 0 a 255      
  }
  delay(100);
}