int lm35 = A0;

void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600); 
}

int valor;
void loop() {  
    valor = analogRead(lm35); //0 - 1023

    Serial.println("Valor leido: " + String(valor));

    valor = (5.0 * valor * 100.0)/1023.0; // °C

    Serial.println("T" + String(valor));

    delay(1000);
}
