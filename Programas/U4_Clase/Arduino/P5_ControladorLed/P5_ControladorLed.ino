int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
  // buffer antes de tomar el valor en serial monitor
  // el Timeout por default es de 1000 milisegundo (1 segundo)
  // .setTimeout(10) cambiamos a 10 milisegundos 
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    // cuantos bytes tiene disponibles el serial (64)
    // si no hay bytes entonces no se realiza el codigo
    int v = Serial.readString().toInt();
    // .readString() leera todos los bytes que se lea posible antes de que sea por defecto
    // .toInt() convertir a entero
    digitalWrite(led,v); // valor ingresado en Serial Monitor controla led 0 = OFF , 1 = ON
  }
}
