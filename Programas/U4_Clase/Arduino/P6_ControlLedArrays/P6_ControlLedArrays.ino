int led[] = {2,3,4,5,6,7,8,9}; //arreglo pines de leds
bool estados[] = {false,false,false,false,false,false,false,false}; //arreglo estados leds (true = ON, false = OFF)

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++){
    pinMode(led[i],OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int idx_led = Serial.readString().toInt()-1;
    estados[idx_led] = !estados[idx_led]; //invierte le valor dentro del arregle estados[]
    //Si True pasa a Falso y viceversa
    digitalWrite(led[idx_led],estados[idx_led]); //(pin a llamar, estado del led (true = ON, false = OFF))
    if(estados[idx_led]){ 
      Serial.println("LED" + String(idx_led + 1) + " encendido");
    } else{
      Serial.println("LED" + String(idx_led + 1) + " apagado");
    }
  }
  delay(100);
}