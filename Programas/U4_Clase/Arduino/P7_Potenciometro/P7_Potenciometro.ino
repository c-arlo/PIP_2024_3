int potenciometro = A3; // Pines analogicos (A0, A1, A2)
//voltage de ref: 5V
//bits resolucion: 10 bits (1024 valores 0 a 1023)
//Pines: 1 - GND / 2 - A0 / 3 - 5V

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //pinMode no se utiliza
  //pin analogico solo es de entrada (INPUT)
}

int valor;
int pvalor = -1;
void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(potenciometro);
  delay(100);
  valor = map(valor, 0, 1023, 0, 100);
  delay(100);
  if (valor != pvalor){
    Serial.println(valor);
    pvalor = valor;
  }
}
