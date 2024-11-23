void setup() {
  // put your setup code here, to run once:
  // modulouart - modulo asincrono universal de transmision y recepcion de datos
  Serial.begin(9600); // inicializa la comunicacion serial
  // valores a los que comunica con otros dispositivos
  // instruccion q inicia la conunicacion dserial entre Arduino y el monitor serial de la computadora
  // estandar 9600 para la computadora
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hola");
  delay(1000); //milsegundos
}

// Tools > Boards > Arduino AVR Boards > Arduino Uno
// Ports > COM 
// Serial monitor imprime
// Sketch vacio para pausar el Arduino
