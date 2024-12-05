int estado = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int valorA;
int valorB;
int b;
void loop() {
  // put your main code here, to run repeatedly:
  switch(estado){
    case 0:
    case 1:
      if(Serial.available()>0){
        int v = Serial.readString().toInt();
        Serial.println("Valor ingresado:" + String(v));
        if(estado == 0){ valorA = v; } else { valorB = v;} 
        estado++;
      }
    break;
    case 2:
      int r = valorA + valorB;
      Serial.println("Suma de A y B: " + String(r));
      estado++;
    case 3:
      Serial.println("Desea repetir?....(1 = SI, 0 = NO)");   
      estado++;
    case 4:
      if(Serial.available()>0){
        Serial.println("Serial disponible?");
        int v = Serial.readString().toInt();
        if(v == 1){ estado = 0; } else { 
          Serial.println("Acaba de llegar al fin!");
          estado++;
        }
      }
  }
  delay(100);
}